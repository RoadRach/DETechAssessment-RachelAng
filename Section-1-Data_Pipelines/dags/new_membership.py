from datetime import datetime, timedelta

# from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task

default_args = {
    'owner': 'Rachel',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(
    dag_id='membership_dag',
    default_args = default_args,
    description='dag for membership etl',
    start_date=datetime(2023, 5, 13),
    schedule_interval='@hourly')

def membership_etl():
    @task()
    def read_csv(ti):
        import pandas as pd

        url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_1.csv'
        url2 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_2.csv'
        url3 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/applications_dataset_test1.csv'
        
        df = pd.concat([pd.read_csv(url2), pd.read_csv(url3)], ignore_index=True)

        print(df)
        ti.xcom_push(df=df)
        # return df
        
    @task()
    def rm_no_name(ti):
        import pandas as pd
        df=ti.xcom_pull(task_ids='read_csv', key='read_csv')
        sdf = df.drop(df[df.name == ''].index)
        udf = df[df.name == ''].index
        print(udf)
        # return df
        print("Sigh")


    read_csv=read_csv()
    rm_no_name = rm_no_name()

membership_dag = membership_etl()
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
    def read_csv():
        import pandas as pd
        import requests
        import glob

        url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_1.csv'
        url2 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_2.csv'
        test_url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/*.csv'
        

        # dfs = pd.read_csv(url)
        # dfs = dfs.append(pd.read_csv(url2))
        
        df = pd.concat(map(pd.read_csv, [url, url2]), ignore_index=True)

        print(df)
        # url2 = 'https://github.com/ameeraadam/DETechAssessment-23/blob/main/applications_dataset_2.csv'

        # for f in url1:
        #     dfs = pd.read_csv(f)
        
        # dfs = pd.read_csv('applications_dataset_1.csv')
        # df = pd.concat(dfs, ignore_index=True)
        
    read_csv=read_csv()

membership_dag = membership_etl()
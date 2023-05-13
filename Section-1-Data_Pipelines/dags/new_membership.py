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
        import os
        import glob

        path = os.path.realpath(__file__)
        dir = os.path.dirname(path)
        dir = dir.replace('dags', 'data')

        all_files = glob.glob(os.path.join(path, "*.csv"))

        for f in all_files:
            dfs = pd.read_csv(f)
        
        df = pd.concat(dfs, ignore_index=True)


        df.head()
        df.info()
        print("Hello World!")


    read_csv=read_csv()

membership_dag = membership_etl()
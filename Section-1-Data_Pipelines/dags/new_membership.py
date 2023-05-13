from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import dag, task
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import os
import re

default_args = {
    'owner': 'Rachel',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

def csv_to_tbl():
    url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_1.csv'
    url2 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_2.csv'
    url3 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/applications_dataset_test1.csv'
#     # conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
    # os.chdir('/Users/homersimpson/Documents/DETechAssessment-RachelAng/DETechAssessment-RachelAng/Section-1-Data_Pipelines/dags')
    df = pd.concat(map(pd.read_csv, [url, url3]), ignore_index=True)
    print(df)
    df.info()
    # df.to_csv('~/Documents/DETechAssessment-RachelAng/DETechAssessment-RachelAng/Section-1-Data_Pipelines/dags')
#     sdf = df.dropna(axis=0, subset=['name'])
#     print(sdf)
#     udf = df.drop
    # jdf = df.to_string(df)

    # postgres_sql_upload = PostgresHook(postgres_conn_id="postgres_localhost")
    # postgres_sql_upload.bulk_load('applications_dataset', jdf)

    # engine = create_engine('postgres://airflow:airflow@localhost:5432/test')
    # df.to_sql('applications_dataset', engine)
    # os.chdir('/Users/homersimpson/Documents/DETechAssessment-RachelAng/DETechAssessment-RachelAng/Section-1-Data_Pipelines/dags')
    # dir = os.getcwd()
    # print(dir)

def data_transform():
    url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_1.csv'
    url2 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_2.csv'
    url3 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/applications_dataset_test1.csv'
#     # conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
    # os.chdir('/Users/homersimpson/Documents/DETechAssessment-RachelAng/DETechAssessment-RachelAng/Section-1-Data_Pipelines/dags')
    df = pd.concat(map(pd.read_csv, [url, url3]), ignore_index=True)

    udf = df[df.name == '']
    sdf = df.drop(df[df.name == ''].index)

    # split name
    # sdf[['first_name', 'last_name']] = df['name'].str.split(' ', expand=True)
    # print(sdf)
    # sdf.info()

    pat = r'(Mrs\.|Mr.\|Ms\.|Dr\.)'

    df['name'] = df['name'].apply(lambda x: re.sub(pat, '', x))
    print(sdf)


with DAG(
    dag_id='dag_with_postgresql_v5',
    default_args=default_args,
    start_date=datetime(2023,5,13),
    schedule_interval='0 * * * *'
) as dag:
    # task1 = PostgresOperator(
    #     task_id='create_postgres_table',
    #     postgres_conn_id='postgres_localhost',
    #     sql="""
    #         create table if not exists dag_runs (
    #             dt date,
    #             dag_id character varying,
    #             primary key (dt, dag_id)
    #         )
    #     """
    # )
    # task2 = PostgresOperator(
    #     task_id='create_applications_table',
    #     postgres_conn_id='postgres_localhost',
    #     sql="""
    #         CREATE TABLE IF NOT EXISTS applications_dataset (
    #             name VARCHAR,
    #             email VARCHAR,
    #             date_of_birth VARCHAR,
    #             mobile_no VARCHAR
    #         )
        
    #     """
    # )

    task3 = PythonOperator(
        task_id='csv_to_tbl',
        python_callable=csv_to_tbl
    )

    task4 = PythonOperator(
        task_id='data_transform',
        python_callable=data_transform
    )

    # task1
    # task2
    task3
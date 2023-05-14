import pandas as pd
import nameparser as HumanName
from datetime import datetime






url = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_1.csv'
url2 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/data/applications_dataset_2.csv'
url3 = 'https://raw.githubusercontent.com/RoadRach/DETechAssessment-RachelAng/main/Section-1-Data_Pipelines/dags/applications_dataset_test1.csv'
#     # conn = psycopg2.connect("host=localhost dbname=postgres user=postgres")
# os.chdir('/Users/homersimpson/Documents/DETechAssessment-RachelAng/DETechAssessment-RachelAng/Section-1-Data_Pipelines/dags')
df = pd.concat(map(pd.read_csv, [url, url3]), ignore_index=True)


import pandas as pd
import nameparser as HumanName
import util_service as us


from nameparser import HumanName
import pandas as pd

csv = ['applications_dataset_1.csv', 'applications_dataset_2.csv']
df = pd.concat(map(pd.read_csv, csv), ignore_index=True)

# archiving applicants with no name
udf = df.loc[df['name'].eq('NaN')]

# dropping applicants with no names
df = df.dropna(subset='name').reset_index(drop=True)

# parse applicant's names
df['parsed_name'] = df['name'].apply(us.p_name)
df['First Name'] = df['parsed_name'].apply(lambda x: x.first)
df['Last Name'] = df['parsed_name'].apply(lambda x: x.last)

# print(df)

# format applicant's dob to 'YYYYMMDD'
df['date_of_birth'] = df['date_of_birth'].apply(us.format_date)

print(df)

# check if applicants are above the age of 18 as of 01 Jan 2022
df['above_18'] = df['date_of_birth'].apply(lambda x: us.above_18(x))

df = df.dropna(subset='date_of_birth').reset_index(drop=True)
df.to_csv('cron_job.csv')
print(df)
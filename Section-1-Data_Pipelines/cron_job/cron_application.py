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

# check if applicant's email are valid, if invalid, set email to 'NaN'
df['email'] = df['email'].apply(lambda x: x if us.is_valid_email(x) else pd.NA)

# check if applicant's mobile are valid, if invalid, set mobile_no to 'NaN'
df['mobile_no'] = df['mobile_no'].apply(lambda x: x if us.is_valid_mobile(x) else pd.NA)

# parse applicant's names
df['parsed_name'] = df['name'].apply(us.p_name)
df['first_name'] = df['parsed_name'].apply(lambda x: x.first)
df['last_name'] = df['parsed_name'].apply(lambda x: x.last)

# print(df)

# format applicant's dob to 'YYYYMMDD'
df['date_of_birth'] = df['date_of_birth'].apply(lambda x: us.format_date(x))

print(df)

df = df.dropna(subset='date_of_birth').reset_index(drop=True)

# check if applicants are above the age of 18 as of 01 Jan 2022
df['above_18'] = df['date_of_birth'].apply(lambda x: us.is_above_18(x))

# df = df.dropna(subset='date_of_birth').reset_index(drop=True)
df.to_csv('cron_job.csv')
# print(df)

df['membership_id'] = df.apply(lambda x: us.get_membership_id(x['last_name'], x['date_of_birth']), axis=1)

print(df)
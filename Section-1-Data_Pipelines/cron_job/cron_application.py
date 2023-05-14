import pandas as pd
import util_service as us
import pandas as pd

csv = ['applications_dataset_1.csv', 'applications_dataset_2.csv']
df = pd.concat(map(pd.read_csv, csv), ignore_index=True)

# archiving applicants with no name
udf = df[df['name'].isnull()].reset_index(drop=True)

# dropping applicants with no names
df = df.dropna(subset='name').reset_index(drop=True)

# check if applicant's email are valid, if invalid, set email to 'NaN' and archive
df['email'] = df['email'].apply(lambda x: x if us.is_valid_email(x) else pd.NA)

print(df)

udf = pd.concat([udf,df['email'].isnull()])
df = df.dropna(subset='email').reset_index(drop=True)

# check if applicant's mobile are valid, if invalid, set mobile_no to 'NaN' and archive
df['mobile_no'] = df['mobile_no'].apply( lambda x: x if us.is_valid_mobile(x) else pd.NA)
udf = pd.concat([udf,df['mobile_no'].isnull()], axis=0)

# parse applicant's names
df['parsed_name'] = df['name'].apply(us.p_name)
df['first_name'] = df['parsed_name'].apply(lambda x: x.first)
df['last_name'] = df['parsed_name'].apply(lambda x: x.last)

# format applicant's dob to 'YYYYMMDD', archive invalid dob
df['date_of_birth'] = df['date_of_birth'].apply(lambda x: us.format_date(x))
udf = pd.concat([udf,df['mobile_no'].isnull()], axis=0)
print(udf)

# have to drop row with invalid dob
df = df.dropna(subset='date_of_birth').reset_index(drop=True)

# check if applicants are above the age of 18 as of 01 Jan 2022
df['above_18'] = df['date_of_birth'].apply(lambda x: True if us.is_above_18(x) else pd.NA)
df = df.dropna(subset='above_18').reset_index(drop=True)

# assign membership id
df['membership_id'] = df.apply(lambda x: us.get_membership_id(x['last_name'], x['date_of_birth']), axis=1)

# # # clean up dataframe
df = df.drop(['name', 'parsed_name'], axis=1)
df = df.dropna().reset_index(drop=True)

# # # output
output_path = 'output/sucessful_applicants.csv'
unsuccessful_output_path = 'output/unsucessful_applicants.csv'

df.to_csv(output_path)
udf.to_csv(unsuccessful_output_path)
# # # print(df)
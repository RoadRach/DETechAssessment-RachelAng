import pandas as pd
import nameparser as HumanName
from datetime import datetime


from nameparser import HumanName
import pandas as pd

csv = ['applications_dataset_1.csv', 'applications_dataset_2.csv']
df = pd.concat(map(pd.read_csv, csv), ignore_index=True)

df = df.dropna(subset='name').reset_index(drop=True)

print(df)

# def p_name(name):
#     return HumanName(name)

# df['parsed_name'] = df['name'].apply(p_name)

# df['First Name'] = df['parsed_name'].apply(lambda x: x.first)
# df['Last Name'] = df['parsed_name'].apply(lambda x: x.last)

# print(df)
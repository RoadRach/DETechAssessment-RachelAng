import pandas as pd
import nameparser as HumanName
import datetime
from datetime import datetime, date


from nameparser import HumanName
import pandas as pd

csv = ['applications_dataset_1.csv', 'applications_dataset_2.csv']
df = pd.concat(map(pd.read_csv, csv), ignore_index=True)

# archiving applicants with no name
udf = df.loc[df['name'].eq('NaN')]

# dropping applicants with no names
df = df.dropna(subset='name').reset_index(drop=True)

# print(df)

# print(udf)

def p_name(name):
    return HumanName(name)

df['parsed_name'] = df['name'].apply(p_name)

df['First Name'] = df['parsed_name'].apply(lambda x: x.first)
df['Last Name'] = df['parsed_name'].apply(lambda x: x.last)

# print(df)

# defining function for formatting dates to 'YYYYMMDD'
def format_date(date_of_birth):
    try:
        # parse the date_of_birth using a list of date formats
        date_obj = None
        for date_format in ['%m/%d/%Y', '%Y/%m/%d', '%Y/%d/%m', '%Y-%m-%d', '%d-%m-%Y', '%Y%d%m', '%d %B %Y', '%Y%m%d']:
            try:
                date_obj = datetime.strptime(date_of_birth, date_format)
                break
            except ValueError:
                pass

        if date_obj is None:
            raise ValueError('Invalid date string ' + date_of_birth)

        # Format the date object to 'YYYYMMDD' format
        formatted_date = date_obj.strftime('%Y%m%d')

    except Exception as e:
        print(f'Error: {e}')
        formatted_date = ''

    return formatted_date

df['date_of_birth'] = df['date_of_birth'].apply(format_date)

print(df)

# def cal_age(date_of_birth, as_of_date):
#     dob = datetime.strptime(date_of_birth, '%Y-%m-%d').date()
#     ref_date = datetime.strptime(as_of_date, '%Y-%m-%d').date()

#     age = ref_date.year-dob.year - ((ref_date.month, ref_date.day) < (dob.month, dob.day))

#     return age

# df['above_18'] = df['date_of_birth'].apply(lambda x: cal_age(x, '2022-01-01'))

# print(df)
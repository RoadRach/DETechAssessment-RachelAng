from datetime import date, datetime
import pandas as pd

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
        formatted_date = pd.NA

    return formatted_date

def cal_age(date_of_birth, as_of_date):
    try:
        dob = datetime.strptime(date_of_birth, '%Y%m%d').date()
        ref_date = datetime.strptime(as_of_date, '%Y%m%d').date()

        age = ref_date.year-dob.year - ((ref_date.month, ref_date.day) < (dob.month, dob.day))

        if date_of_birth is None:
            raise ValueError('Invalid date string ' + date_of_birth)

    except Exception as e:
        print(f'Error: {e}')
        age = pd.NA
    
    return (age>18)
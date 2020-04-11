# records.py
"""formats address records and eliminates records with missing critical fields."""
import re
import pandas as pd

# get_file
df = pd.read_csv('../wk4/MOCK_DATA.csv', sep=',', header=0)


def get_formatted_phone(value):
    """using regular expression fullmatch, tries to apply the phone number format or ignores.
    accepted input phone numbers will be xxxxxxxxxx or xxx-xxx-xxxx"""
    phone = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    normal = re.fullmatch(r'\d{3}-\d{3}-\d{4}', value)
    if phone:
        return '-'.join(phone.groups())
    elif normal:
        return normal.string
    else:
        return ''


def get_formatted_zip(value):
    """using regular expression fullmatch, tries to apply the zip code format or ignores
    accepted input zip codes will be xxxxx or xxxxxxxxx"""
    zip_four = re.fullmatch(r'(\d{5})(\d{4})', value)
    normal_zip = re.fullmatch(r'(\d{5})', value)
    if zip_four:
        return '-'.join(zip_four.groups())
    elif normal_zip:
        return normal_zip.string
    else:
        return ''


def format_data(data):
    """Formats the data frame passed as an argument by calling the other formatting methods"""
    data.columns = ['First Name', 'Last Name', 'Zip Code', 'Phone Number']
    data.fillna('', inplace=True) # anything with NaN will be filled with blank string
    formatted_phone = data['Phone Number'].map(get_formatted_phone)
    data['Phone Number'] = formatted_phone
    formatted_zip = data['Zip Code'].map(get_formatted_zip)
    data['Zip Code'] = formatted_zip


format_data(df)
print(df.to_string(index=False))

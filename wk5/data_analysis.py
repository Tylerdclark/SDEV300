# data_analysis.py
"""allows a user to load one of two CSV files and then perform histogram analysis and plots"""
import pandas as pd


def menu():
    """Collects user input to call other methods with"""
    return int(input('Select the file you want to analyze:\n1. Population Data\n2. Housing Data\n3. Exit the Program'))


print('******** Welcome to the Python Data Analysis App ********')


user_input = menu()


def population_from_file():
    pass


def pd_population_data():
    return pd.read_csv('../wk5/PopChange.csv', sep=',', header=0)


def pd_housing_data():
    return pd.read_csv('../wk5/Housing.csv', sep=',', header=0)


while user_input != 3:

    if user_input == 1:
        print(pd_population_data())
        user_input = menu()

    if user_input == 2:
        pd_housing_data()
        user_input = menu()


print('******** Thank you for using the Python Data Analysis App ********')

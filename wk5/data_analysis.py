# data_analysis.py
"""allows a user to load one of two CSV files and then perform histogram analysis and plots"""


def menu():
    """Collects user input to call other methods with"""
    return int(input('Select the file you want to analyze:\n1. Population Data\n2. Housing Data\n3. Exit the Program'))


print('******** Welcome to the Python Data Analysis App ********')


user_input = menu()


def population_data():
    pass


def housing_data():
    pass


while user_input != 3:

    if user_input == 1:
        population_data()
        user_input = menu()

    if user_input == 2:
        housing_data()
        user_input = menu()


print('******** Thank you for using the Python Data Analysis App ********')

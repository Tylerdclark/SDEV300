# data_analysis.py
"""allows a user to load one of two CSV files and then perform histogram analysis and plots"""
import csv
import matplotlib.pyplot as plt
import numpy as np

display_count = 0
populations = list()
houses = list()


class PopChange:
    """Defines a class for the data of the PopChange.csv"""
    def __init__(self, var1, var2, var3):
        self.april_pop = var1
        self.july_pop = var2
        self.change_pop = var3


class Housing:
    """Defines a class for the data of the Housing.csv"""
    def __init__(self, var1, var2, var3, var4):
        self.age = var1
        self.bedrooms = var2
        self.weight = var3
        self.utility = var4


def populate_populations():
    """Fills up a list with population objects"""
    try:
        with open('../wk5/PopChange.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                populations.append(PopChange(int(row[4]), int(row[5]), int(row[6])))
    except FileNotFoundError:
        print('File was not found!')


def populate_houses():
    """Fills up the list with housing objects"""
    try:
        with open('../wk5/Housing.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:  # for some reason it is taking these as strings
                houses.append(Housing(float(row[0]), float(row[1]), float(row[5]), float(row[6])))
    except FileNotFoundError:
        print('File was not found!')


def menu():
    """Collects user input to call other methods with"""
    try:
        return int(input('Select the file you want to analyze:\n1. Population Data\n2. Housing'
                         ' Data\n3. Exit the Program\n'))
    except ValueError:
        print('Please use Integers')


def population_menu():
    """displays a menu for population data if 1 is given as user_input"""
    print('You have entered Population data')
    choice = input('Select the Column you want to analyze:\na. Pop Apr 1\nb. Pop Jul 1\nc. '
                   'Change Pop\nd. Exit Column\n')
    if choice == 'a':
        print('You have selected Pop Apr 1')
        analyse_stats([population.april_pop for population in populations])
        population_menu()
    elif choice == 'b':
        print('You have selected Pop Jul 1')
        analyse_stats([population.july_pop for population in populations])
        population_menu()
    elif choice == 'c':
        print('You have selected Pop change')
        analyse_stats([population.change_pop for population in populations])
        population_menu()
    elif choice == 'd':
        return
    else:
        population_menu()


def houses_menu():
    """Displays a menu for housing data if 2 is given as user-input"""
    print('You have entered Housing data')
    choice = input('Select the Column you want to analyze:\na. Age\nb. Bedrooms\nc. '
                   'Weight\nd. Utility\ne. Exit Column\n')
    if choice == 'a':
        print('You have selected Housing age')
        analyse_stats([house.age for house in houses])
        houses_menu()
    elif choice == 'b':
        print('You have selected Housing bedrooms')
        analyse_stats([house.bedrooms for house in houses])
        houses_menu()
    elif choice == 'c':
        print('You have selected Housing weight')
        analyse_stats([house.weight for house in houses])
        houses_menu()
    elif choice == 'd':
        print('You have selected Housing utility')
        analyse_stats([house.utility for house in houses])
        houses_menu()
    elif choice == 'e':
        return
    else:
        houses_menu()


def analyse_stats(column_list):
    """Utility function to call others"""
    print('The statistics for this column are:')
    column_statistics(column_list)
    plot_hist(column_list)


def column_statistics(column_list):
    """Prints a formatted string of the statistics of a column"""
    print(f'Count: {len(column_list)}\nMean: {np.mean(column_list):.1f}\nStandard Deviation: {np.std(column_list):.1f}'
          f'\nMin: {np.min(column_list)}\nMax: {np.max(column_list)}')


def plot_hist(column_list):
    """Plots a histogram from column data passed as a list"""
    global display_count
    display_count += 1
    plt.hist(column_list, len(column_list), density=True, facecolor='b', alpha=0.75)
    plt.grid(True)
    plt.savefig(f'../wk5/display{display_count}.png')
    plt.show()


print('******** Welcome to the Python Data Analysis App ********')

user_input = menu()


while user_input != 3:

    if user_input == 1:
        populate_populations()
        population_menu()
        user_input = menu()

    if user_input == 2:
        populate_houses()
        houses_menu()
        user_input = menu()

print('******** Thank you for using the Python Data Analysis App ********')

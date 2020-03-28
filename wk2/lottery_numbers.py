# lottery_numbers.py
"""Produces a random 3 and 4 digit lottery number"""
import random

user_choice = 0  # initialize the user selection at first run


def menu():
    """Displays a menu and collects the input from the user"""
    return int(input("\nSelect from the following menu: \n1. Generate 3-Digit Lottery number \n2. Generate 4-Digit "
                     "Lottery number\n3. Exit the Application"))


def get_lotto(num):
    """returns the amount of random numbers passed as argument as a tuple"""
    return random.sample(range(0, 10), num)


print('**** Welcome to the Pick-3, Pick-4 lottery number generator ****')

while user_choice != 3:

    user_choice = menu()  # each run of while loop will grab choice at beginning

    if user_choice == 1:
        val1, val2, val3 = get_lotto(3)  # unpack tuple returned by method
        print('\nYour 3 digit lottery number is:\n')
        print(f'{val1} {val2} {val3}')
        continue   # continue will reenter the while loop, going back to top

    elif user_choice == 2:
        val1, val2, val3, val4 = get_lotto(4)  # unpack tuple returned by method
        print('\nYour 4 digit lottery number is:\n')
        print(f'{val1} {val2} {val3} {val4}')
        continue

    else:  # to catch any response other than 1, 2 or 3
        print('\nNot a valid response!')
        continue

print('\nThanks for trying the Lottery application')  # displays once while loop is terminated

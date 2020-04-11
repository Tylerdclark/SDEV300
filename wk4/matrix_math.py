# matrix_math.py
"""Allows user to do math on matrices"""
import numpy as np

# initialize User selection
user_selection = 'Y'


def menu():
    """Takes user input to determine whether to continue or not"""
    return input('Do you want to play the Matrix Game?\nEnter Y for Yes or N for No:\n').upper()


def input_array():
    """Prompts a user for input before create an 3 by 3 array"""
    try:
        integers_input = input('Please enter 9 integers delimited by spaces.\n')
        integer_array = np.array(integers_input.split()).reshape(3, 3)
        return integer_array.astype(int)
    except ValueError:
        print('Invalid input, please try again')
        return input_array()


def print_array(array):
    """prints ever element in each column"""
    for row in array:
        for element in row:
            print(element, end=' ')
        print()


def matrix_operation_options():
    """Gets the input from the user regarding the matrix operation"""
    return input('Select a Matrix Operation from the list below:\na. Addition\n'
                 'b. Subtraction\nc. Matrix Multiplication\nd. Element by element multiplication\n').upper()


def show_result(array):
    """Prints the array, transpose and mean values of row and column"""
    print_array(array)
    print('The Transpose is:')
    print_array(array.T)
    print('The row and column mean values of the results are:')
    val1, val2, val3 = array.mean(axis=1)
    print(f'Row: {val1}, {val2}, {val3}')
    val1, val2, val3 = array.mean(axis=0)
    print(f'Column: {val1}, {val2}, {val3}')


print('********** Welcome to the Python Matrix Application ***********')
while user_selection != 'N':
    user_selection = menu()
    if user_selection == 'Y':
        array_one = input_array()
        print_array(array_one)
        array_two = input_array()
        print_array(array_two)
        matrix_selection = matrix_operation_options()
        if matrix_selection == 'A':
            print('You have selected Addition. The results are:')
            result_array = np.add(array_one, array_two)
            show_result(result_array)
        elif matrix_selection == 'B':
            print('You have selected Subtraction. The results are:')
            result_array = np.subtract(array_one, array_two)
            show_result(result_array)
        elif matrix_selection == 'C':
            print('You have selected Matrix Multiplication. The results are:')
            result_array = np.matmul(array_one, array_two)
            show_result(result_array)
        elif matrix_selection == 'D':
            print('You have selected Element by element multiplication. The results are:')
            result_array = np.multiply(array_one, array_two)
            show_result(result_array)

print('Thank for playing the matrix game!')

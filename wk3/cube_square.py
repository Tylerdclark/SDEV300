# cube_square.py
"""determines the union, intersection and difference of the square and cube of integers ranging from 1 to 100"""

user_selection = -1


def menu():
    try:
        return int(input('\n1. Display the Square and Cube for Integers ranging from 1 to 100\n2. Search the sets for a'
                         ' specific Integer and display the Square and Cube values\n3. Display the Union of Square and '
                         'Cube sets\n4. Display the Intersection of Square and Cube sets\n5. Display the Difference of '
                         'Square and Cube sets\n6. Exit the program\n'))
    except ValueError:
        print('Please use integers!')


def square():
    """Using comprehension to return a set of squares from 1 to 100"""
    return {item ** 2 for item in range(1, 101)}


def cube():
    """Using comprehension to return a set of cubes from 1 to 100"""
    return {item ** 3 for item in range(1, 101)}


def display_sets():
    """Sort the sets before assigning them, zipping them and printing"""
    squared_set = sorted(square())
    cubed_set = sorted(cube())
    print('x^2 and x^3 over [1,100]:')
    for i, j in zip(squared_set, cubed_set):
        print(f'{i}   {j:}')


def search_sets():
    """Gets input before searching the sets for the input"""
    try:  # put in a try catch for the int cast
        set_search = int(input('What Integer would you like to search for within the sets'))
        squared = set_search ** 2
        cubed = set_search ** 3
        if squared in square() and cubed in cube():
            print(f'Integer:{set_search}, Square value: {squared}, Cube value: {cubed}')
        else:
            print('Integer not in sets')
    except ValueError:
        print('Please use Integers')


def show_union_set():
    """prints the union of the two sets"""
    union_set = square() | cube()  # using the set operators for the following selections
    print('Union of the sets x^2 and x^3 over [1,100]:')
    for i in sorted(union_set):  # display sorted
        print(i)


def show_intersection_set():
    """prints the intersection of the two sets"""
    intersection_set = square() & cube()
    print('Intersection of the sets x^2 and x^3 over [1,100]:')
    for i in sorted(intersection_set):
        print(i)


def show_difference_set():
    """prints the difference of the two sets"""
    print('Difference of the sets x^2 and x^3 over [1,100]:')
    difference_set = square() - cube()
    print('These numbers are in x^2 but not in x^3')
    for i in sorted(difference_set):
        print(i)
    difference_set = cube() - square() # There are two distinct differences, so providing both
    print('These numbers are in x^3 but not in x^2')
    for i in sorted(difference_set):
        print(i)


print('Welcome to the Square and Cube from 1 to 100 Program!')
print('*** Please choose from the following menu ***')

while user_selection != 6:

    user_selection = menu()
    print()

    if user_selection == 1:
        display_sets()
        continue

    if user_selection == 2:
        search_sets()
        continue

    if user_selection == 3:
        show_union_set()
        continue

    if user_selection == 4:
        show_intersection_set()
        continue

    if user_selection == 5:
        show_difference_set()
        continue

    if user_selection == 6:
        break
    else:
        print('Not a valid response!')

print('Thank you for using the Square and Cube from 1 to 100 Program!')

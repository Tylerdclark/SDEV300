# state_bird_flower.py
"""Display, sort and update a List of U.S States containing the State Capital and State Bird"""

user_selection = -1

database = {'Alabama': ['Montgomery', 'Yellowhammer', 'Camellia'],
            'Alaska': ['Juneau', 'Willow Ptarmigan', 'Forget Me Not'],
            'Arizona': ['Phoenix', 'Cactus Wren', 'Saguaro Cactus Blossom'],
            'Arkansas': ['Little Rock', 'Mockingbird', 'Apple Blossom'],
            'California': ['Sacramento', 'California Valley Quail', 'California Poppy'],
            'Colorado': ['Denver', 'Lark Bunting', 'White and Lavender Columbine'],
            'Connecticut': ['Hartford', 'Robin', 'Mountain Laurel'],
            'Delaware': ['Dover', 'Blue Hen', 'Peach Blossom'],
            'Florida': ['Tallahassee', 'Mockingbird', 'Orange Blossom'],
            'Georgia': ['Atlanta', 'Brown Thrasher', 'Cherokee Rose'],
            'Hawaii': ['Honolulu', 'Nene', 'Hibiscus'],
            'Idaho': ['Boise', 'Mountain Bluebird', 'Syringa'],
            'Illinois': ['Springfield', 'Cardinal', 'Purple Violet'],
            'Indiana': ['Indianapolis', 'Cardinal', 'Peony'],
            'Iowa': ['Des Moines', 'Eastern Goldfinch', 'Wild Prairie Rose'],
            'Kansas': ['Topeka', 'Western Meadowlark', 'Sunflower'],
            'Kentucky': ['Frankfort', 'Cardinal', 'Goldenrod'],
            'Louisiana': ['Baton Rouge', 'Eastern Brown Pelican', 'Magnolia'],
            'Maine': ['Augusta', 'Chickadee', 'White Pine Cone and Tassel'],
            'Maryland': ['Annapolis', 'Baltimore Oriole', 'Black-Eyed Susan'],
            'Massachusetts': ['Boston', 'Chickadee', 'Mayflower'],
            'Michigan': ['Lansing', 'Robin', 'Apple Blossom'],
            'Minnesota': ['Saint Paul', 'Common Loon', 'Pink and White Lady Slipper'],
            'Mississippi': ['Jackson', 'Mockingbird', 'Magnolia'],
            'Missouri': ['Jefferson City', 'Bluebird', 'White Hawthorn Blossom'],
            'Montana': ['Helena', 'Western Meadowlark', 'Bitterroot'],
            'Nebraska': ['Lincoln', 'Western Meadowlark', 'Goldenrod'],
            'Nevada': ['Carson City', 'Mountain Bluebird', 'Sagebrush'],
            'New Hampshire': ['Concord', 'Purple Finch', 'Purple Lilac'],
            'New Jersey': ['Trenton', 'Eastern Goldfinch', 'Violet'],
            'New Mexico': ['Santa Fe', 'Roadrunner', 'Yucca Flower'],
            'New York': ['Albany', 'Bluebird', 'Rose'],
            'North Carolina': ['Raleigh', 'Cardinal', 'Dogwood'],
            'North Dakota': ['Bismarck', 'Western Meadowlark', 'Wild Prairie Rose'],
            'Ohio': ['Columbus', 'Cardinal', 'Scarlet Carnation'],
            'Oklahoma': ['Oklahoma City', 'Scissor-Tailed Flycatcher', 'Mistletoe'],
            'Oregon': ['Salem', 'Western Meadowlark', 'Oregon Grape'],
            'Pennsylvania': ['Harrisburg', 'Ruffed Grouse', 'Mountain Laurel'],
            'Rhode Island': ['Providence', 'Rhode Island Red', 'Violet'],
            'South Carolina': ['Columbia', 'Great Carolina Wren', 'Yellow Jessamine'],
            'South Dakota': ['Pierre', 'Ring-Necked Pheasant', 'Pasque Flower'],
            'Tennessee': ['Nashville', 'Mockingbird', 'Iris'],
            'Texas': ['Austin', 'Mockingbird', 'Bluebonnet'],
            'Utah': ['Salt Lake City', 'California Seagull', 'Sego Lily'],
            'Vermont': ['Montpelier', 'Hermit Thrush', 'Red Clover'],
            'Virginia': ['Richmond', 'Cardinal', 'Dogwood'],
            'Washington': ['Olympia', 'Willow Goldfinch', 'Pink Rhododendron'],
            'West Virginia': ['Charleston', 'Cardinal', 'Rhododendron'],
            'Wisconsin': ['Madison', 'Robin', 'Wood Violet'],
            'Wyoming': ['Cheyenne', 'Western Meadowlark', 'Indian Paintbrush']
            }


def menu():
    """takes in the int value to be used by other methods and logic"""
    try:
        return int(input('1. Display all U.S. States in Alphabetical order along with Capital and Flower \n2. Search '
                         'for a specific state and display the appropriate Capital and Bird \n3. Update a Bird for a '
                         'specific state \n4. Exit the program\n'))
    except ValueError:
        print('please use Integer for menu selection')  # this may be redundant with the else statement @ bottom


def show_user(state, state_info):
    """Utility method used by other methods to print state info to output"""
    capital, bird, flower = state_info
    print(f'\n{state}: Capital: {capital}, Bird: {bird}, Flower: {flower}\n')


def display():
    """displays every element in the database by calling show_user() over all"""
    for entry in sorted(database):
        show_user(entry, database.get(entry))
    print('\n')


def search(state):
    """Returns the values for the given key else returns not found"""
    entry = state.title()
    if entry in database:
        return database[entry]
    else:
        return 'Not found!'


print('Welcome to the State Bird and Flower Program!')
print('*** Please choose from the following menu ***\n')
# main logic
while user_selection != 4:
    user_selection = menu()
    # use display function before continuing to another loop of the while loop
    if user_selection == 1:
        display()
        continue

    if user_selection == 2:  # convert to title case before searching with input
        state_input = input('Which state would you like to the info for?\n').title()
        result = search(state_input)
        if result != 'Not found!':
            show_user(state_input, result)
            continue
        else:
            print(result + '\n')  # this will simply print 'not found'
            continue

    if user_selection == 3:  # convert to title case before searching with input
        bird_change_selection = input('Which state would you like to change the bird for?\n').title()
        result = search(bird_change_selection)
        if result != 'Not Found!':
            print(f'Current bird: {database[bird_change_selection][1]}')  # access second element directly
            new_bird = input('What is the new bird?\n')
            database[bird_change_selection][1] = new_bird
            print("*** New Bird updated ***")
            show_user(bird_change_selection, database[bird_change_selection])  # display to user before carrying on
            continue
        else:
            print(result)  # this will simply print 'not found'
            continue

    if user_selection == 4:
        break

    else:  # to catch everything else
        print('\nNot a valid response!\n')
        continue

print('*** Thank you for using the State Bird and Flower Program! ***')
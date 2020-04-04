# state_bird_flower.py
"""Display, sort and update a List of U.S States containing the State Capital and State Bird"""

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
    int(input('1. Display all U.S. States in Alphabetical order along with Capital and Flower \n\
    2. Search for a specific state and display the appropriate Capital and Bird \n\
    3. Update a Bird for a specific state   4. Exit the program'))


def display():
    for entry in database:
        capital, bird, flower = database.get(entry)
        return f'{entry}: Capital: {capital}, Bird: {bird}, Flower: {flower} '


def search(term):
    entry = term.title()
    if entry in database:
        capital, bird, flower = database['Nevada']
        return f'{entry}: Capital: {capital}, Bird: {bird}, Flower: {flower} '
    else:
        return 'Not found!'




# display()
print(search("nevada"))

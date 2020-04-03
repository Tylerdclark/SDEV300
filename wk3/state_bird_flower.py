# state_bird_flower.py
"""Display, sort and update a List of U.S States containing the State Capital and State Bird"""

ALABAMA = ('Alabama', 'Montgomery', 'Yellowhammer', 'Camellia')
ALASKA = ('Alaska', 'Juneau', 'Willow Ptarmigan', 'Forget Me Not')
ARIZONA = ('Arizona', 'Phoenix', 'Cactus Wren', 'Saguaro Cactus Blossom')
ARKANSAS = ('Arizona', 'Little Rock', 'Mockingbird', 'Apple Blossom')
CALIFORNIA = ('California', 'Sacramento', 'California Valley Quail', 'California Poppy')
COLORADO = ('Colorado', 'Denver', 'Lark Bunting', 'White and Lavender Columbine')
CONNECTICUT = ('Connecticut', 'Hartford', 'Robin', 'Mountain Laurel')
DELAWARE = ('Delaware', 'Dover', 'Blue Hen', 'Peach Blossom')
FLORIDA = ('Florida', 'Tallahassee', 'Mockingbird', 'Orange Blossom')
GEORGIA = ('Georgia', 'Atlanta', 'Brown Thrasher', 'Cherokee Rose')
HAWAII = ('Hawaii', 'Honolulu', 'Nene', 'Hibiscus')
IDAHO = ('Idaho', 'Boise', 'Mountain Bluebird', 'Syringa')
ILLINOIS = ('Illinois', 'Springfield', 'Cardinal', 'Purple Violet')
INDIANA = ('Indiana', 'Indianapolis', 'Cardinal', 'Peony')
IOWA = ('Iowa', 'Des Moines', 'Eastern Goldfinch', 'Wild Prairie Rose')
KANSAS = ('Kansas', 'Topeka', 'Western Meadowlark', 'Sunflower')
KENTUCKY = ('Kentucky', 'Frankfort', 'Cardinal', 'Goldenrod')
LOUISIANA = ('Louisiana', 'Baton Rouge', 'Eastern Brown Pelican', 'Magnolia')
MAINE = ('Maine', 'Augusta', 'Chickadee', 'White Pine Cone and Tassel')
MARYLAND = ('Maryland', 'Annapolis', 'Baltimore Oriole', 'Black-Eyed Susan')
MASSACHUSETTS = ('Massachusetts', 'Boston', 'Chickadee', 'Mayflower')
MICHIGAN = ('Michigan', 'Lansing', 'Robin', 'Apple Blossom')
MINNESOTA = ('Minnesota', 'Saint Paul', 'Common Loon', 'Pink and White Lady Slipper')
MISSISSIPPI = ('Mississippi', 'Jackson', 'Mockingbird', 'Magnolia')
MISSOURI = ('Missouri', 'Jefferson City', 'Bluebird', 'White Hawthorn Blossom')
MONTANA = ('Montana', 'Helena', 'Western Meadowlark', 'Bitterroot')
NEBRASKA = ('Nebraska', 'Lincoln', 'Western Meadowlark', 'Goldenrod')
NEVADA = ('Nevada', 'Carson City', 'Mountain Bluebird', 'Sagebrush')
NEW_HAMPSHIRE = ('New Hampshire', 'Concord', 'Purple Finch', 'Purple Lilac')
NEW_JERSEY = ('New Jersey', 'Trenton', 'Eastern Goldfinch', 'Violet')
NEW_MEXICO = ('New Mexico', 'Santa Fe', 'Roadrunner', 'Yucca Flower')
NEW_YORK = ('New York', 'Albany', 'Bluebird', 'Rose')
NORTH_CAROLINA = ('North Carolina', 'Raleigh', 'Cardinal', 'Dogwood')
NORTH_DAKOTA = ('North Dakota', 'Bismarck', 'Western Meadowlark', 'Wild Prairie Rose')
OHIO = ('Ohio', 'Columbus', 'Cardinal', 'Scarlet Carnation')
OKLAHOMA = ('Oklahoma', 'Oklahoma City', 'Scissor-Tailed Flycatcher', 'Mistletoe')
OREGON = ('Oregon', 'Salem', 'Western Meadowlark', 'Oregon Grape')
PENNSYLVANIA = ('Pennsylvania', 'Harrisburg', 'Ruffed Grouse', 'Mountain Laurel')
RHODE_ISLAND = ('Rhode Island', 'Providence', 'Rhode Island Red', 'Violet')
SOUTH_CAROLINA = ('South Carolina', 'Columbia', 'Great Carolina Wren', 'Yellow Jessamine')
SOUTH_DAKOTA = ('South Dakota', 'Pierre', 'Ring-Necked Pheasant', 'Pasque Flower')
TENNESSEE = ('Tennessee', 'Nashville', 'Mockingbird', 'Iris')
TEXAS = ('Texas', 'Austin', 'Mockingbird', 'Bluebonnet')
UTAH = ('Utah', 'Salt Lake City', 'California Seagull', 'Sego Lily')
VERMONT = ('Vermont', 'Montpelier', 'Hermit Thrush', 'Red Clover')
VIRGINIA = ('Virginia', 'Richmond', 'Cardinal', 'Dogwood')
WASHINGTON = ('Washington', 'Olympia', 'Willow Goldfinch', 'Pink Rhododendron')
WEST_VIRGINIA = ('West Virginia', 'Charleston', 'Cardinal', 'Rhododendron')
WISCONSIN = ('Wisconsin', 'Madison', 'Robin', 'Wood Violet')
WYOMING = ('Wyoming', 'Cheyenne', 'Western Meadowlark', 'Indian Paintbrush')

database = [ALABAMA, ALASKA, ARIZONA, ARKANSAS, CALIFORNIA, COLORADO, CONNECTICUT, DELAWARE, FLORIDA, GEORGIA, HAWAII,
            IDAHO, ILLINOIS, INDIANA, IOWA, KANSAS, KENTUCKY, LOUISIANA, MAINE, MARYLAND, MASSACHUSETTS, MICHIGAN,
            MINNESOTA, MISSISSIPPI, MISSOURI, MONTANA, NEBRASKA, NEVADA, NEW_HAMPSHIRE, NEW_JERSEY, NEW_MEXICO,
            NEW_YORK, NORTH_CAROLINA, NORTH_DAKOTA, OHIO, OKLAHOMA, OREGON, PENNSYLVANIA, RHODE_ISLAND, SOUTH_CAROLINA,
            SOUTH_DAKOTA, TENNESSEE, TEXAS, UTAH, VERMONT, VIRGINIA, WASHINGTON, WEST_VIRGINIA, WISCONSIN, WYOMING]


def menu():
    int(input('1. Display all U.S. States in Alphabetical order along with Capital and Flower \n\
    2. Search for a specific state and display the appropriate Capital and Bird \n\
    3. Update a Bird for a specific state   4. Exit the program'))


def display():
    for entry in database:
        state, capital, bird, flower = entry
        print(f"{state}: Capital: {capital}, Bird: {bird}, Flower: {flower} ")


display()

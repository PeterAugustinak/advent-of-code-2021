"""
ADVENT OF CODE DAY 5 - HYDROTHERMAL VENTURE
Full description: https://adventofcode.com/2021/day/5
"""

# reading input data for the exercise
with open("src/inputs/day5_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

# general functions
def create_coordinates_dictionary(data):
    """"Create coordinate dictionary from rough data in for of {coordinate_num: {x1: num, y1: num, x2: num, y2: num}}"""
    # intitialize coordinates dictionary
    coordinates_dict = {}
    coordinates_lst = [string.split('-> ') for string in data]
    coordinates_main = []
    for coordinates in coordinates_lst:
        coor_lst = []
        for coordinate in coordinates:
            coor = [int(coor) for coor in coordinate.split(',')]
            coor_lst.append(coor)
        coordinates_main.append(coor_lst)
    for enum, item in enumerate(coordinates_main):
        coordinates_dict[enum] = {'x1': item[0][0], 'y1': item[0][1], 'x2': item[1][0], 'y2': item[1][1]}
    return coordinates_dict

def show_coordinates(coordinates_dict):
    """Show coordinates in pretty output"""
    for coor_num, coor_data in coordinates_dict.items():
        print(f"{coor_num}: {coor_data}")

def filter_coordinates_dict_to_hor_ver_only(coordinates_dict):
    """Filter only coordinates where either x1 == x2 or y1 == y2"""
    filtered_coordinates = {}
    for name, data in coordinates_dict.items():
        if (data['x1'] == data['x2']) or (data['y1'] == data['y2']):
            filtered_coordinates[name] = data
    return filtered_coordinates

def traverse_coordinates(coordinates):
    """Traverse through all coordinates and send every coordinate to fill occupied places"""
    for coordinate in coordinates.values():
        fill_occupied_places_based_on_coordinate(coordinate)

def fill_occupied_places_based_on_coordinate(coordinate):
    """Determines if the line is horizontal (x) or vertical (y) and based on that call function to 'draw line' between two positions"""
    if coordinate['x1'] == coordinate['x2']:
        point = coordinate['x1']
        val1, val2 = coordinate['y1'], coordinate['y2']
        mark = 'x'
    elif coordinate['y1'] == coordinate['y2']:
        point = coordinate['y1']
        val1, val2 = coordinate['x1'], coordinate['x2']
        mark = 'y'
    update_occupied_places(val1, val2, point, mark)

position_map = {}

def update_occupied_places(val1, val2, point, mark):
    """Draw line between two places and add 1 point for every coordinate of the line to position map (as occupied place)"""
    global position_map
    min_val = min(val1, val2)
    max_val = max(val1, val2)
    for val in range(min_val, max_val + 1):
        if mark == 'x':
            occupated_coordinates = f"{point}-{val}"
        elif mark == 'y':
            occupated_coordinates = f"{val}-{point}"
        try:
            position_map[occupated_coordinates] += 1
        except KeyError:
            position_map[occupated_coordinates] = 1
 
def find_number_of_overlapped_places(position_map):
    """Check every occupied place in map and if place has value > 1 - means place is overlapped by more coordinates, adds 1 to counter"""
    number_of_overlapped_places = 0
    for value in position_map.values():
        if value > 1:
            number_of_overlapped_places += 1
    return number_of_overlapped_places

# PART I.
all_coordinates = create_coordinates_dictionary(data)
filtered_coordinates = filter_coordinates_dict_to_hor_ver_only(all_coordinates)
# fill position map
traverse_coordinates(filtered_coordinates)
count_of_overlapped_places = find_number_of_overlapped_places(position_map)
print(f"PART I. Number of overlapped places: {count_of_overlapped_places}")





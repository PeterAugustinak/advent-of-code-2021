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

def filter_coordinates(coordinates_dict):
    """Filter only coordinates where either x1 == x2 or y1 == y2"""
    filtered_coordinates_direct = {}
    filtered_coordinates_diagonal = {}
    for name, data in coordinates_dict.items():
        if (data['x1'] == data['x2']) or (data['y1'] == data['y2']):
            filtered_coordinates_direct[name] = data
        else:
            filtered_coordinates_diagonal[name] = data
    return filtered_coordinates_direct, filtered_coordinates_diagonal

position_map_direct = {}
position_map_diagonal = {}

def update_occupied_places_direct(coordinate):
    """Draw line between two places and add 1 point for every coordinate of the line to position map (as occupied place)"""
    val1, val2, point, mark = resolve_direct_coordinate_values(coordinate)
    min_val = min(val1, val2)
    max_val = max(val1, val2)
    for val in range(min_val, max_val + 1):
        if mark == 'x':
            occupated_coordinates = f"{point}-{val}"
        elif mark == 'y':
            occupated_coordinates = f"{val}-{point}"
        try:
            position_map_direct[occupated_coordinates] += 1
        except KeyError:
            position_map_direct[occupated_coordinates] = 1
  
def resolve_direct_coordinate_values(coordinate):
    """Determines if the line is horizontal (x) or vertical (y) and based on that call function to 'draw line' between two positions"""
    if coordinate['x1'] == coordinate['x2']:
        point = coordinate['x1']
        val1, val2 = coordinate['y1'], coordinate['y2']
        mark = 'x'
    elif coordinate['y1'] == coordinate['y2']:
        point = coordinate['y1']
        val1, val2 = coordinate['x1'], coordinate['x2']
        mark = 'y'
    return val1, val2, point, mark

def update_occupied_places_diagonal(coordinate):
    """Draw line between two places diagonally and add 1 point for every coordinate of the line to position map (as occupied place)"""
    min_x = min(coordinate['x1'], coordinate['x2'])
    max_x = max(coordinate['x1'], coordinate['x2'])
    max_y = max(coordinate['y1'], coordinate['y2'])

    # find distance between x1 and x2 (or y1 and y2 - it doesn't matter as diagonals are always exactly in 45 degrees)
    for inc in range(max_x - min_x + 1):
        # now decide if increase is going + or - based on how is coordinate defined
        inc_x = -inc if coordinate['x1'] == max_x else inc
        inc_y = -inc if coordinate['y1'] == max_y else inc

        occupated_coordinates = f"{coordinate['x1'] + inc_x}-{coordinate['y1'] + inc_y}"
        try:
            position_map_diagonal[occupated_coordinates] += 1
        except KeyError:
            position_map_diagonal[occupated_coordinates] = 1
 
def find_number_of_overlapped_places(position_map):
    """Check every occupied place in map and if place has value > 1 - means place is overlapped by more coordinates, adds 1 to counter"""
    number_of_overlapped_places = 0

    for value in position_map.values():
        if value > 1:
            number_of_overlapped_places += 1
    return number_of_overlapped_places

all_coordinates = create_coordinates_dictionary(data)
filtered_coordinates_direct, filtered_coordinates_diagonal = filter_coordinates(all_coordinates)

# # PART I.
for coordinate in filtered_coordinates_direct.values():
    update_occupied_places_direct(coordinate)
count_of_overlapped_places_direct = find_number_of_overlapped_places(position_map_direct)
print(f"PART I. Number of overlapped places by horizontal/vertical lines only: {count_of_overlapped_places_direct}")

# PART II.
for coordinate in filtered_coordinates_diagonal.values():
    update_occupied_places_diagonal(coordinate)

count_of_overlapped_places_diagonal = find_number_of_overlapped_places(position_map_diagonal)
print(f"Number of overlapped places by diagonal lines only: {count_of_overlapped_places_diagonal}")

# count all overlapped occupied places by merging both maps
position_map_total = position_map_direct

for key, value in position_map_diagonal.items():
    try:
        position_map_total[key] += value
    except KeyError:
        position_map_total[key] = value

count_of_overlapped_places_total = find_number_of_overlapped_places(position_map_total)
print(f"PART II. Number of overlapped places TOTAL: {count_of_overlapped_places_total}")

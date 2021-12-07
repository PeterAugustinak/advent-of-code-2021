"""
ADVENT OF CODE DAY 7 - TREACHERY OF WHALES
Full description: https://adventofcode.com/2021/day/7
"""

# reading input data for the exercise
with open("src/inputs/day7_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

crab_position_lst = [int(position) for position in data[0].split(',')]


# general functions
def count_to_desired_position(desired_position, crab_position):
    """This counts the distance for signle position to desired position"""
    distance = abs(crab_position - desired_position) 
    return distance

def show_all_positions_with_distances_sorted(distances):
    """Shows list of distances sorted by the smallest"""
    distances_sorted = sort_distances_lst(distances)
    for position, distance in distances_sorted:
        print(f"{position}: {distance}")

def get_smallest_distance_value(distances):
    distances_sorted = sort_distances_lst(distances)
    return distances_sorted[0][1]

def sort_distances_lst(distances_lst):
        distances_sorted = sorted(distances_lst.items(), key=lambda x: x[1])
        return distances_sorted


# PART I.
distances = {}
for desired_position in crab_position_lst:
    total_distance_for_desired_position = 0
    for crab_position in crab_position_lst:
        distance_single_crab_to_desired_position = count_to_desired_position(desired_position, crab_position)
        total_distance_for_desired_position += distance_single_crab_to_desired_position
    distances[desired_position] = total_distance_for_desired_position

# show_all_positions_with_distances_sorted(distances)
smallest = get_smallest_distance_value(distances)
print(f"PART I.: The least fuel possible to sort crabs is: {smallest}.")










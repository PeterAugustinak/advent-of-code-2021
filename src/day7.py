"""
ADVENT OF CODE DAY 7 - TREACHERY OF WHALES
Full description: https://adventofcode.com/2021/day/7
"""
import sys

# reading input data for the exercise
with open("src/inputs/day7_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

crab_position_lst = [int(position) for position in data[0].split(',')]
# Recursion limit must be raised otherwise count_factor() will stop before done
sys.setrecursionlimit(max(crab_position_lst) * 2)

## interresting helpers to check
# print(max(crab_position_lst, key = crab_position_lst.count))
# positionz_not_present = [position for position in range(max(crab_position_lst)) if position not in crab_position_lst]
# print(len(set(crab_position_lst)))
# print(len(positionz_not_present))

# general functions
def count_to_desired_position(desired_position, crab_position):
    """This counts the distance for signle position to desired position"""
    distance = abs(crab_position - desired_position) 
    return distance


def count_to_desired_position_with_factor_count(desired_position, crab_position):
    """This counts the distance for signle position to desired position with factor"""
    distance_normal = abs(crab_position - desired_position)
    distance_real = count_factor(distance_normal)
    return distance_real


def show_all_positions_with_distances_sorted(distances):
    """Shows list of distances sorted by the smallest"""
    distances_sorted = sort_distances_lst(distances)
    for position, distance in distances_sorted:
        print(f"{position}: {distance}")


def get_smallest_distance_value(distances):
    """Returns smallest distance from distances list"""
    distances_sorted = sort_distances_lst(distances)
    return distances_sorted[0][1]


def sort_distances_lst(distances_lst):
    """Returns sorted distance list"""
    distances_sorted = sorted(distances_lst.items(), key=lambda x: x[1])
    return distances_sorted


def count_factor(result, number=0):
    """Count factor for particular distance (number) and returns the result"""
    result += number
    if number > 1:
        return count_factor(result, number - 1)
    else:
        return result 


def count_diststances(function, crab_position_lst):
    """
    Iterates through all positions in crab position list and then through all crabs to count
    poisitions for every crab to every position
    """
    distances_dict = {}
    for desired_position in range(0, max(crab_position_lst)):
        total_distance_for_desired_position = 0
        for crab_position in crab_position_lst:
            distance_single_crab_to_desired_position = function(desired_position, crab_position)
            total_distance_for_desired_position += distance_single_crab_to_desired_position
        distances_dict[desired_position] = total_distance_for_desired_position
    return distances_dict


# PART I.
distances = count_diststances(count_to_desired_position, crab_position_lst)
# show_all_positions_with_distances_sorted(distances)
smallest = get_smallest_distance_value(distances)
print(f"PART I.: The least fuel possible to sort crabs is: {smallest}.")

# # PART II.
distances_real = count_diststances(count_to_desired_position_with_factor_count, crab_position_lst)
# show_all_positions_with_distances_sorted(distances_real)
smallest_real = get_smallest_distance_value(distances_real)
print(f"PART II.: The REAL least fuel possible to sort crabs is: {smallest_real}.")

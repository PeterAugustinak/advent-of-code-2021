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


def count_factor(number, result=0):
    """Count factor for particular distance (number) and returns the result"""
    result += number
    if number > 1:
        return count_factor(number - 1, result)
    else:
        return result 


def find_shortest_distance(function, crab_position_lst):
    """
    Iterates through all positions in crab position list and then through all crabs to count
    poisitions for every crab to every position
    """
    shortest_distance = 0 
    for desired_position in range(0, max(crab_position_lst)):
        current_distance_for_desired_position = 0
        for crab_position in crab_position_lst:
            distance_single_crab_to_desired_position = function(desired_position, crab_position)
            current_distance_for_desired_position += distance_single_crab_to_desired_position
        shortest_distance = compare_shortest_vs_current(shortest_distance, current_distance_for_desired_position)
    return shortest_distance


def compare_shortest_vs_current(shortest, current):
    """Compares current shortest distance vs current counted distance and returns 'winning' value"""
    return shortest if (shortest < current and shortest != 0) else current


# PART I.
def part_one(crab_position_lst):
    distance = find_shortest_distance(count_to_desired_position, crab_position_lst)
    print(f"PART I.: The least fuel possible to sort crabs is: {distance}.")

# # PART II.
def part_two(crab_position_lst):
    distance_real = find_shortest_distance(count_to_desired_position_with_factor_count, crab_position_lst)
    print(f"PART II.: The REAL least fuel possible to sort crabs is: {distance_real}.")



if __name__ == "__main__":
    part_one(crab_position_lst)
    part_two(crab_position_lst)

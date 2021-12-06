"""
ADVENT OF CODE DAY 6 - LANTERNFISH
Full description: https://adventofcode.com/2021/day/6
"""

# reading input data for the exercise
from typing import final


with open("src/inputs/day6_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

lanterfish_start_lst = [int(fish) for fish in data[0].split(',')]
# general functions

day_left = 256

def iterate_over_fish_lst(fish_lst):
    global day_left
    new_fish_lst = []
    for fish in sorted(fish_lst):
        if fish == 0:
            new_fish_lst.append(6)
            new_fish_lst.append(8)
        else:
            new_fish_lst.append(fish +- 1)
    day_left -= 1
    while day_left:
        print(day_left, len(new_fish_lst))
        return iterate_over_fish_lst(new_fish_lst)
    else:
        return new_fish_lst

final_lanterfish_lst = iterate_over_fish_lst(lanterfish_start_lst)
print(len(final_lanterfish_lst))



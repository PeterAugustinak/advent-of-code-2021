"""
ADVENT OF CODE DAY 6 - LANTERNFISH
Full description: https://adventofcode.com/2021/day/6
"""
from itertools import chain


# reading input data for the exercise
with open("src/inputs/day6_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

lanterfish_start_lst = [int(fish) for fish in data[0].split(',')]

# general functions
def iterate_over_fish_lst(day_left, fish_lst=None):
    """Recursive function to iterate throgh newly generated list"""
    if not fish_lst:
        fish_lst = []
    fish_lst = sorted(fish_lst)
    new_fish_lst_1 = (6 for fish in fish_lst if fish == 0)
    new_fish_lst_2 = (8 for fish in fish_lst if fish == 0)
    new_fish_lst_3 = (fish-1 for fish in fish_lst if fish != 0)
    new_fish_lst = list(new_fish_lst_1) + list(new_fish_lst_2) + list(new_fish_lst_3)

    day_left -= 1
    while day_left:
        print(day_left, len(new_fish_lst))
        return iterate_over_fish_lst(day_left, new_fish_lst)
    else:
        return new_fish_lst

final_lanterfish_lst = iterate_over_fish_lst(120, lanterfish_start_lst)
print(len(final_lanterfish_lst))






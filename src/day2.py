"""
ADVENT OF CODE DAY 2 - DIVE!
Full description: https://adventofcode.com/2021/day/2
"""

# reading input data for the exercise
with open("src/inputs/day2_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

forward = 0
deep = 0

# PART I.
for instruction in data:
    single_data = instruction.split()
    if single_data[0] == 'up':
        decrease = -int((single_data[1]))
        deep += decrease
    elif single_data[0] == 'down':
        increase = int(single_data[1])
        deep += increase
    elif single_data[0] == 'forward':
        increase = int(single_data[1])
        forward += increase
    
final_depth = forward * deep
print(f"DONE! Final depth is {final_depth}!")

# PART II.
forward = 0
deep = 0
aim = 0

for instruction in data:
    single_data = instruction.split()
    if single_data[0] == 'up':
        decrease = -int((single_data[1]))
        aim += decrease
    elif single_data[0] == 'down':
        increase = int(single_data[1])
        aim += increase
    elif single_data[0] == 'forward':
        increase = int(single_data[1])
        forward += increase
        deep += aim * increase

real_final_depth = forward * deep
print(f"DONE! Real final depth is {real_final_depth}!")

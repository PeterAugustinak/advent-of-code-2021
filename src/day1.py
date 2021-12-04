"""
ADVENT OF CODE DAY 1 - DONAR SWEEP
Full description: https://adventofcode.com/2021/day/1
"""

# reading input data for the exercise
with open("src/inputs/day1_input.txt", "r") as f:
    content = [line.rstrip('\n') for line in f]
    
# PART I.
larger_meassurement = 0
for measurement in range(len(content)-1):
    if int(content[measurement+1]) > int(content[measurement]):
        larger_meassurement += 1

print(f"DONE! {larger_meassurement} are larger!")

# PART II.
measures = [int(measure) for measure in content]
real_measures = [sum(measures[rep:rep+3]) for rep in range(len(measures)-2)]

precise_larger_meassurement = 0
for measurement in range(len(real_measures)-1):
    if int(real_measures[measurement+1]) > int(real_measures[measurement]):
        precise_larger_meassurement += 1

print(f"DONE! {precise_larger_meassurement} are actully larger!")

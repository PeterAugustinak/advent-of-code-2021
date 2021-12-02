with open("src/day2_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

forward = 0
deep = 0

# part#1
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
        
print(forward * deep)

# part#2
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

print(forward * deep)


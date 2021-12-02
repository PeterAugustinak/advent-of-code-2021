with open("src/day1_input.txt", "r") as f:
    content = [line.rstrip('\n') for line in f]
    
# part#1
larger_meassurement = 0
for measurement in range(len(content)-1):
    if int(content[measurement+1]) > int(content[measurement]):
        larger_meassurement += 1

print(larger_meassurement)

# part#2
measures = [int(measure) for measure in content]
real_measures = [sum(measures[rep:rep+3]) for rep in range(len(measures)-2)]

larger_meassurement = 0
for measurement in range(len(real_measures)-1):
    if int(real_measures[measurement+1]) > int(real_measures[measurement]):
        larger_meassurement += 1

print(larger_meassurement)
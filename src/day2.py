with open("src/day1_input.txt", "r") as f:
    measures = [line.rstrip('\n') for line in f]

measures = [int(measure) for measure in measures]
real_measures = [sum(measures[rep:rep+3]) for rep in range(len(measures)-2)]

print(len(measures))
print(len(real_measures))
print(measures[0])
print(real_measures[0])

larger_meassurement = 0
for measurement in range(len(real_measures)-1):
    if int(real_measures[measurement+1]) > int(real_measures[measurement]):
        larger_meassurement += 1

print(larger_meassurement)

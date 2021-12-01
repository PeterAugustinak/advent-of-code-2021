import os
import os


with open("src/day1_input.txt", "r") as f:
    
    content = [line.rstrip('\n') for line in f]
    print(content)
    
larger_meassurement = 0
for measurement in range(len(content)-1):
    if int(content[measurement+1]) > int(content[measurement]):
        larger_meassurement += 1

print(len(content))
print(larger_meassurement)

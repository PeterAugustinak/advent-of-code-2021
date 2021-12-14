"""
ADVENT OF CODE DAY - EXTENDED POLYMERIZATION
Full description: https://adventofcode.com/2021/day/14
"""
from collections import Counter


# TEMPLATED FUNCTIONS
def parse(day):
    """Parse input"""
    with open(f"src/inputs/day{day}_input.txt", "r") as f:
        data = [line.rstrip('\n') for line in f]
    return data

insertion_dict = None

def part1(data):
    """Solve part 1"""
    polymer_template = data[0]
    global insertion_dict
    insertion_dict = parse_insertion_as_dict(data[2:])
    polymer = build_polymer(polymer_template, 10)
    most_common_num, least_common_num = find_occurence(polymer)

    return most_common_num - least_common_num

def part2(data):
    """Solve part 2"""
    polymer_template = data[0]
    polymer = build_polymer(polymer_template, 40)
    most_common_num, least_common_num = find_occurence(polymer)

    return most_common_num - least_common_num

def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    # solution2 = part2(data)

    return [solution1]# , solution2

# SOLUTION FUNCTIONS
def parse_insertion_as_dict(data):
    """Will parse insertion data and make key-value pairs of dictionary."""
    insertion_dict = {x[:2]: x[-1] for x in data}
    return insertion_dict

def build_polymer(polymer, num_of_steps):
    """Recursively goes through raising polymer and inserting elements"""
    while num_of_steps:
        new_polymer = ''
        for pos in range(0, len(polymer)-1):
            shifre = f"{polymer[pos]}{polymer[pos+1]}"
            insertion = insertion_dict[shifre]
            polymer_part = f"{polymer[pos]}{insertion}"
            new_polymer += polymer_part
        return build_polymer(f"{new_polymer}{polymer[-1]}", num_of_steps-1)
    else:
        return polymer

def find_occurence(polymer):
    """Finds most and least common number of occurence of element in list"""
    counter = Counter(polymer)
    most_common = counter.most_common(1)[0][1]
    least_common = counter.most_common()[-1][1]
    return most_common, least_common


if __name__ == "__main__":
    solutions = solve(14)
    print("\n".join(str(solution) for solution in solutions))

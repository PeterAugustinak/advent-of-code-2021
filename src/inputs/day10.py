"""
ADVENT OF CODE DAY 10 - SYNTAX SCORING
Full description: https://adventofcode.com/2021/day/10
"""
import pathlib
import sys


# TEMPLATED FUNCTIONS
def parse(day):
    """Parse input"""
    with open(f"src/inputs/day{day}_input.txt", "r") as f:
        data = [line.rstrip('\n') for line in f]
    return data

def part1(data):
    """Solve part 1"""

    total_value = 0
    
    for line in data:
        remaining_line = strip_line_from_correct_chunks(line)
        bad_char = find_bad_char(remaining_line)
        if bad_char:
            value = value_bad_char(bad_char)
            total_value += value

    return total_value


def part2(data):
    """Solve part 2"""
 
def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# SOLUTION FUNCTIONS
def strip_line_from_correct_chunks(line):
    chuncks = ('<>', '()', str('{}'), '[]')
    new_line = line
    for chunck in chuncks:
        part_line = new_line.replace(chunck, '')
        new_line = part_line

    if len(new_line) < len(line): 
        return strip_line_from_correct_chunks(new_line)
    else:
        return new_line


def find_bad_char(remaining_line):
    for char in remaining_line:
        if char in ('>', ')', '}', ']'):
            return char


def value_bad_char(bad_char):
    char_values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137        
    }

    return char_values.get(bad_char)


if __name__ == "__main__":
    solutions = solve(10)
    print("\n".join(str(solution) for solution in solutions))

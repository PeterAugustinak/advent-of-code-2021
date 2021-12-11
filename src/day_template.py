"""
ADVENT OF CODE DAY 
Full description: https://adventofcode.com/2021/day/
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
 

def part2(data):
    """Solve part 2"""
 
def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# SOLUTION FUNCTIONS






if __name__ == "__main__":
    solutions = solve()
    print("\n".join(str(solution) for solution in solutions))



"""
ADVENT OF CODE DAY 9 - SMOKE BASIN
Full description: https://adventofcode.com/2021/day/8
"""
import pathlib
import sys

def parse(day):
    """Parse input"""
    with open(f"src/inputs/day{day}_input.txt", "r") as f:
        data = [line.rstrip('\n') for line in f]
    return data

def part1(data):
    """Solve part 1"""
    line_data = [line for line in data]
    
    total_sum = 0
    for line_num in range(0, len(line_data)):
        above = line_data[line_num-1] if line_num != 0 else None
        current = line_data[line_num]
        try:
            under = line_data[line_num+1]
        except IndexError:
            under = None
    
        lines = [above, current, under]
        if not lines[0]:
            total_sum += check_heat_zones_first(lines[1:])
        elif not lines[2]:
            total_sum += check_heat_zones_last(lines[:2])
        else:
            total_sum += check_heat_zones_standard(lines)


    return total_sum


def check_heat_zones_first(lines):
    nums = []
    rng = len(lines[1])-1
    for num_pos in range(0, rng+1):
        current = int(lines[0][num_pos])+1
        if num_pos == 0:
            if lines[0][num_pos] < lines[0][num_pos+1] and lines[0][num_pos] < lines[1][num_pos]:
                nums.append(current)
        elif num_pos == rng:
            if lines[0][num_pos] < lines[0][num_pos-1] and lines[0][num_pos] < lines[1][num_pos]:
                nums.append(current)
        else:
            if lines[0][num_pos] < lines[0][num_pos-1] and lines[0][num_pos] < lines[0][num_pos+1] and lines[0][num_pos] < lines[1][num_pos]:
                nums.append(current)

    return sum(nums)

def check_heat_zones_last(lines):
    nums = []
    rng = len(lines[1])-1
    for num_pos in range(0, rng+1):
        current = int(lines[1][num_pos])+1
        if num_pos == 0:
            if lines[1][num_pos] < lines[1][num_pos+1] and lines[1][num_pos] < lines[0][num_pos]:
                nums.append(current)
        elif num_pos == rng:
            if lines[1][num_pos] < lines[1][num_pos-1] and lines[1][num_pos] < lines[0][num_pos]:
                nums.append(current)
        else:
            if lines[1][num_pos] < lines[1][num_pos-1] and lines[1][num_pos] < lines[1][num_pos+1] and lines[1][num_pos] < lines[0][num_pos]:
                nums.append(current)
    return sum(nums)

def check_heat_zones_standard(lines):
    nums = []
    rng = len(lines[1])-1
    for num_pos in range(0, rng+1):
        current = int(lines[1][num_pos])+1
        if num_pos == 0:
            if lines[1][num_pos] < lines[1][num_pos+1] and lines[1][num_pos] < lines[0][num_pos] and lines[1][num_pos] < lines[2][num_pos]:
                nums.append(current)
        elif num_pos == rng:
            if lines[1][num_pos] < lines[1][num_pos-1] and lines[1][num_pos] < lines[0][num_pos] and lines[1][num_pos] < lines[2][num_pos]:
                nums.append(current)
        else:
            if lines[1][num_pos] < lines[1][num_pos-1] and lines[1][num_pos] < lines[1][num_pos+1] and lines[1][num_pos] < lines[0][num_pos] and lines[1][num_pos] < lines[2][num_pos]:
                nums.append(current)
    return sum(nums)


def part2(data):
    """Solve part 2"""



def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(9)
    print("\n".join(str(solution) for solution in solutions))

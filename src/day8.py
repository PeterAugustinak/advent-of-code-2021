"""
ADVENT OF CODE DAY 8 - SEVEN SEGMENT SEARCH
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
    shifre = parse_digits_and_shifre(data)[1]
    return decode_digits(shifre)


def parse_digits_and_shifre(data):
    digits = []
    shifre = []
    for message in data:
        splited_message = message.split(' | ')
        digits.append(splited_message[0].split())
        shifre.append(splited_message[1].split())
    
    return digits, shifre


def decode_digits(shifre):
    counter = 0
    for part in shifre:
        for digit in part:
            real_digit = len(set(digit))
            if real_digit == 2 or real_digit == 4 or real_digit == 7 or real_digit == 3:
                counter += 1

    return counter


def part2(data):
    """Solve part 2"""
    pass

def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(8)
    print("\n".join(str(solution) for solution in solutions))
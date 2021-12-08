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
    
    counter = 0
    for part in shifre:
        for digit in part:
            counter += decode_digits(digit)[0]
    return counter


def part2(data):
    """Solve part 2"""
    shifre = parse_digits_and_shifre(data)[1]

    digit_lst = []
    for part in shifre:
        line_digit = ''
        for digit in part:
            line_digit += decode_digits(digit)[1]
            line_digit += decode_complicated_digits(digit)
        digit_lst.append(line_digit)

    total = sum(int(num) for num in digit_lst if num)
    return total


def parse_digits_and_shifre(data):
    digits = []
    shifre = []
    for message in data:
        splited_message = message.split(' | ')
        digits.append(splited_message[0].split())
        shifre.append(splited_message[1].split())
    
    return digits, shifre


def decode_digits(entry):
    counter = 0
    string = ''

    real_digit = len(set(entry))

    if real_digit == 2:
        string += '1'
        counter += 1
    elif real_digit == 3:
        string += '7'
        counter += 1
    elif real_digit == 4:
        string += '4'
        counter += 1
    elif real_digit == 7:
        string += '8'
        counter += 1

    return counter, string

def decode_complicated_digits(entry):
    entry = sorted(entry)
    string =''
    two = 'dafgc'
    three = 'dafbc'
    five = 'defbc'
    six = 'defbcg'
    nine = 'defabc'
    zero = 'dabcge'

    if entry == sorted(two):
        string += '2'
    if entry == sorted(three):
        string += '3'
    if entry == sorted(five):
        string += '5'
    if entry == sorted(six):
        string += '6'
    if entry == sorted(nine):
        string += '9'
    if entry == sorted(zero):
        string += '0'

    return string


def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(8)
    print("\n".join(str(solution) for solution in solutions))
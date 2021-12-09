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
    digits = parse_digits_and_shifre(data)[0]
    line_shifre_lst = []
    for line in digits:
        line_shifre = {}
        for digit in line:
            line_shifre.update(decode_digits(digit)[2])
        line_shifre_lst.append(line_shifre)


    translated_digit_lst = []
    lines_to_translate = parse_digits_and_shifre(data)[1]
    for shifre, line in zip(line_shifre_lst, lines_to_translate):
        line_digit = translate_digit(shifre, line)
        translated_digit_lst.append(line_digit)
    
    return sum(int(number) for number in translated_digit_lst if number)


def translate_digit(shifre, line):

    two = f"{shifre['upper']}{shifre['right_upper']}{shifre['middle']}{shifre['left_lower']}{shifre['lower']}"
    three = f"{shifre['upper']}{shifre['right_upper']}{shifre['middle']}{shifre['right_lower']}{shifre['lower']}"
    five = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['right_lower']}{shifre['lower']}"
    six = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['left_lower']}{shifre['lower']}{shifre['right_lower']}"
    nine = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['left_upper']}{shifre['lower']}{shifre['right_lower']}" 
    zero = f"{shifre['upper']}{shifre['left_upper']}{shifre['left_lower']}{shifre['lower']}{shifre['right_lower']}"

    string = '' # total digit for the current line
    
    # print(f"Shifre: {shifre}")
    for digit in line:
        # print(f"Line: {digit}")
        entry_sorted = sorted(digit)
        real_digit = len(digit)

        if entry_sorted == sorted(two):
            string += '2'
        if entry_sorted == sorted(three):
            string += '3'
        if entry_sorted == sorted(five):
            string += '5'
        if entry_sorted == sorted(six):
            string += '6'
        if entry_sorted == sorted(nine):
            string += '9'
        if entry_sorted == sorted(zero):
            string += '0'
        if real_digit == 2:
            string += '1'
        elif real_digit == 3:
            string += '7'
        elif real_digit == 4:
            string += '4'
        elif real_digit == 7:
            string += '8'
    
    return string
    

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
    wires = {}

    real_digit = len(entry)

    if real_digit == 2:
        string += '1'
        counter += 1    
        wires['right_upper'] = entry[0]
        wires['right_lower'] = entry[1]
    if real_digit == 3:
        string += '7'
        counter += 1
        wires['upper'] = entry[0]
    if real_digit == 4:
        string += '4'
        counter += 1
        wires['left_upper'] = entry[0]
        wires['middle'] = entry[2]
    if real_digit == 7:
        string += '8'
        counter += 1
        wires['left_lower'] = entry[1]
        # wires['upper'] = entry[3]
        wires['lower'] = entry[0]
  
    return counter, string, wires


def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(8)
    print("\n".join(str(solution) for solution in solutions))

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
    right_digits = parse_digits_and_shifre(data)[1]
    total_counter = 0
 
    for line in right_digits:
        total_counter += count_clear_digits(line)

    return total_counter


def part2(data):
    """Solve part 2"""
    # at first take a left part of the line and resolve shifre for that line 
    digits = parse_digits_and_shifre(data)[0]
    line_shifre_lst = []
    for line in digits:
        clear_digits = decode_clear_digits(line)
        line_shifre = get_shifre_for_single_line(line, clear_digits)
        line_shifre_lst.append(line_shifre)

    # then take a shifre for single line and right part of the line and translate digits on this part
    translated_digit_lst = []
    lines_to_translate = parse_digits_and_shifre(data)[1]
    for shifre, line in zip(line_shifre_lst, lines_to_translate):
        line_digit = translate_digit(shifre, line)
        translated_digit_lst.append(line_digit)
    
    # sum resulted digits of all lines
    return sum(number for number in translated_digit_lst if number)


def parse_digits_and_shifre(data):
    """Parse digits for a single line divided for left ("learning") part and right ("answer") part"""
    left_digits = []
    right_digits = []
    for message in data:
        splited_message = message.split(' | ')
        left_digits.append(splited_message[0].split())
        right_digits.append(splited_message[1].split())
    
    return left_digits, right_digits


def count_clear_digits(line):
    """Count 'clear' digits in a given line"""
    counter = 0

    for digit in line:
        real_digit = len(digit)
        counter += 1 if real_digit == 2 else 0
        counter += 1 if real_digit == 3 else 0
        counter += 1 if real_digit == 4 else 0
        counter += 1 if real_digit == 7 else 0

    return counter

def decode_clear_digits(line):
    """Returns string for every clear digit (the digit with unice number of elements)"""
    one = ''
    seven = ''
    four = ''
    eight = ''

    for digit in line:
        real_digit = len(digit)
        if not one:
            if real_digit == 2:
                one = digit
        if not seven:
            if real_digit == 3:
                seven = digit
        if not four:
            if real_digit == 4:
                four = digit
        if not eight:
            if real_digit == 7:
                eight = digit
  
    return [one, seven, four, eight]


def get_shifre_for_single_line(line, clear_digits):
    """Returns unique shifre for single line based on continuously known elements"""
    one = clear_digits[0]
    seven = clear_digits[1]
    four = clear_digits[2]
    eight = clear_digits[3]
    two_five = set(digit for digit in line if len(digit) == 5 and not set(one).issubset(digit))

    # find two and five
    elem = set(eight) - set(seven) - set(four)
    for num in two_five:
        if set(elem).issubset(set(num)):
            two = num
        else:
            five = num

    line_shifre = {}
    upper = set(seven) - set(one)    
    left_lower = set(eight) - set(four) - set(five)
    left_upper = set(eight) - set(seven) - set(two)
    right_upper = set(eight) - set(five) - left_lower
    right_lower = set(eight) - set(two) - left_upper
    lower = set(eight) - set(four) - upper - left_lower
    middle = set(eight) - upper - lower - left_upper - left_lower - right_upper - right_lower

    line_shifre = {
        'upper': ''.join(upper),
        'left_upper': ''.join(left_upper),
        'right_upper': ''.join(right_upper),
        'middle': ''.join(middle),
        'left_lower': ''.join(left_lower),
        'right_lower': ''.join(right_lower),
        'lower': ''.join(lower)
    }
    return line_shifre


def translate_digit(shifre, line):
    """Take a digit and compare to a digit created from shifre. If it matches, add digit to a line digit string"""

    one = f"{shifre['right_upper']}{shifre['right_lower']}"
    two = f"{shifre['upper']}{shifre['right_upper']}{shifre['middle']}{shifre['left_lower']}{shifre['lower']}"
    three = f"{shifre['upper']}{shifre['right_upper']}{shifre['middle']}{shifre['right_lower']}{shifre['lower']}"
    four = f"{shifre['left_upper']}{shifre['right_upper']}{shifre['middle']}{shifre['right_lower']}"
    five = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['right_lower']}{shifre['lower']}"
    six = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['left_lower']}{shifre['lower']}{shifre['right_lower']}"
    seven = f"{shifre['upper']}{shifre['right_upper']}{shifre['right_lower']}"
    eight =f"{shifre['upper']}{shifre['left_upper']}{shifre['right_upper']}{shifre['middle']}{shifre['left_lower']}{shifre['lower']}{shifre['right_lower']}"  
    nine = f"{shifre['upper']}{shifre['left_upper']}{shifre['middle']}{shifre['right_upper']}{shifre['lower']}{shifre['right_lower']}" 
    zero = f"{shifre['upper']}{shifre['left_upper']}{shifre['right_upper']}{shifre['left_lower']}{shifre['right_lower']}{shifre['lower']}"

    string = '' # total digit for the current line

    wires = [zero, one, two, three, four, five, six, seven, eight, nine]

    for digit in line:
        digit = sorted(digit)
        if digit == sorted(wires[0]):
            string += '0'
        if digit == sorted(wires[1]):
            string += '1'
        if digit == sorted(wires[2]):
            string += '2'
        if digit == sorted(wires[3]):
            string += '3'
        if digit == sorted(wires[4]):
            string += '4'
        if digit == sorted(wires[5]):
            string += '5'
        if digit == sorted(wires[6]):
            string += '6'
        if digit == sorted(wires[7]):
            string += '7'
        if digit == sorted(wires[8]):
            string += '8'
        if digit == sorted(wires[9]):
            string += '9'

    return int(string)


def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    solutions = solve(8)
    print("\n".join(str(solution) for solution in solutions))

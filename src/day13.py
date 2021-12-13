"""
ADVENT OF CODE DAY - TRANSPARENT ORIGAMI
Full description: https://adventofcode.com/2021/day/13
"""


# TEMPLATED FUNCTIONS
def parse(day):
    """Parse input"""
    with open(f"src/inputs/day{day}_input.txt", "r") as f:
        data = [line.rstrip('\n') for line in f]
    return data

def part1(data):
    """Solve part 1"""
    paper = draw_paper(data)
    fold_instructions = get_fold_instructions(data)
    folded_paper = get_folded_paper(paper, [fold_instructions[0]])

    total_dots = count_dots(folded_paper)
    return total_dots

def part2(data):
    """Solve part 2"""
    paper = draw_paper(data)
    fold_instructions = get_fold_instructions(data)
    folded_paper = get_folded_paper(paper, fold_instructions)

    make_pretty_code(folded_paper)

def make_pretty_code(folded_paper):
    """Filter resulted folded paper to better readability of final code."""
    for row in folded_paper:
        row = ''.join(row)
        code = row.replace('.', ' ')
        print(code)

def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# SOLUTION FUNCTIONS
def draw_paper(data):
    """Creates paper (grid) with # in x and y positions based on instructions"""
    instructions = data[:-13]
    instructions = [instruction.split(',') for instruction in instructions]

    x_lst = [int(instruction[0]) for instruction in instructions]
    y_lst = [int(instruction[1]) for instruction in instructions]

    paper_right_bottom = (max(x_lst), max(y_lst))

    paper = []
    for row in range(0, paper_right_bottom[1]+2):
        row = []
        for _ in range(0, paper_right_bottom[0]+1):
            row.append('.')
        paper.append(row)
    
    for instruction in instructions:
        paper[int(instruction[1])][int(instruction[0])] = '#'

    return paper

def get_fold_instructions(data):
    """
    Take all the instructions from the end of the data and split it for single instructions with fold
    direction and coordination to where to fold.
    """
    folds = data[-12:]
    items = [item.split()[2].split('=') for item in folds]

    return items
    
def get_folded_paper(folded_paper, fold_instructions):
    """Recursively takes folded paper and fold it based on instruction"""

    if fold_instructions:
        if fold_instructions[0][0] == 'x':
            folded_paper = fold_left_right(folded_paper, fold_instructions[0][1])

        if fold_instructions[0][0] == 'y':
            folded_paper = fold_bottom_up(folded_paper, fold_instructions[0][1])

        fold_instructions = fold_instructions[1:]
        return get_folded_paper(folded_paper, fold_instructions)
    else:
        return folded_paper

def fold_left_right(paper, on_position):
    """Folds every row on the paper left to right"""

    on_position = int(on_position)

    folded_paper = []
    for row in paper:
        first_half = row[:on_position]
        second_half = row[on_position+1:]
        second_half = second_half[::-1]

        folded_row = first_half
        for pos, i in enumerate(second_half):
            if i == '#':
                folded_row[pos] = i
        folded_paper.append(folded_row)
    
    return folded_paper

def fold_bottom_up(paper, on_position):
    """Folds bottom half of the list to up"""

    on_position = int(on_position)
    paper_len = len(paper)

    if paper_len % 2 == 0:
        first_half = paper[:on_position]
        second_half = paper[on_position:]

    else:
        first_half = paper[:on_position]
        second_half = paper[on_position+1:]
   
    second_half = second_half[::-1]
    folded_paper = first_half

    for row_num, row in enumerate(second_half):
        for char_pos, char in enumerate(row):
            if char == '#':
                folded_paper[row_num][char_pos] = char
 
    return folded_paper

def count_dots(folded_paper):
    """Count all the present dots (#) in current fold."""
    dots = 0
    for row in folded_paper:
        for elem in row:
            if elem == '#':
                dots += 1

    return dots


if __name__ == "__main__":
    solutions = solve(13)
    print("\n".join(str(solution) for solution in solutions))
    
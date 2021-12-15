"""
ADVENT OF CODE DAY 
Full description: https://adventofcode.com/2021/day/15
"""

# TEMPLATED FUNCTIONS
def parse(day):
    """Parse input"""
    with open(f"src/inputs/day{day}_input.txt", "r") as f:
        data = [line.rstrip('\n') for line in f]
    return data

def part1(data):
    """Solve part 1"""
    labyrint = [row for row in data]
    total_risk = navigate_via_labyrint(labyrint)
    return total_risk


def part2(data):
    """Solve part 2"""
 
def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# SOLUTION FUNCTIONS
def navigate_via_labyrint(labyrint, current_position=(0, 0), total_risk=0, current_direction='right'):
    """
    Navigating through labyrint by recursively calling determine_next_step_in_labyrint method
    and counting the total risk number.
    """
    while current_position:
        next_position, total_risk, current_direction = determine_next_step_in_labyrint(labyrint, current_position, current_direction, total_risk)
        return navigate_via_labyrint(labyrint, next_position, total_risk, current_direction)
    else:
        return total_risk


def determine_next_step_in_labyrint(labyrint,  current_position, current_direction, total_risk):
    """
    Determines what is the best next step with follwing rules:
    - only can go to the right or down - means i+1 or row[1][i]
    - if the same numbers are left and row, favor the current moving direction
    """
    current_direction = 'right'
    r, c = current_position

    right_position = (r, c+1)
    down_position = (r+1, c)

    try:
        right_risk = int(labyrint[r][c+1])
    except IndexError:
        right_risk = None
    try:
        down_risk = int(labyrint[r+1][c])
    except IndexError:
        down_risk = None

    if right_risk and down_risk:
        next_position, risk, current_direction = evaluate_next_step_if_both_exist(right_risk, down_risk, right_position, down_position, current_direction)
    else:
        next_position, risk, current_direction = evaluate_next_step_when_border(right_risk, down_risk, right_position, down_position, )

    print(risk)
    total_risk += risk
    return next_position, total_risk, current_direction

def evaluate_next_step_if_both_exist(right_risk, down_risk, right_position, down_position, current_direction):
    """If both right and left step exists, it determines what next step is better."""

    if right_risk < down_risk:
        return right_position, right_risk, 'right'     
    elif down_risk < right_risk:
        return down_position, down_risk, 'down'
    elif right_risk == down_risk:
        if current_direction == 'right':
            return right_position, right_risk, 'right'
        elif current_direction == 'down':
            return down_position, down_risk, 'down'

def evaluate_next_step_when_border(right_risk, down_risk, right_position, down_position):
    """If there is most right of most down position, or the final step (right down), then it evaluates specifically."""
    if right_risk:
        return right_position, right_risk, 'right'     
    elif down_risk:
        return down_position, down_risk, 'down'
    else:
        return None, 0, None
    









if __name__ == "__main__":
    solutions = solve(15)
    print("\n".join(str(solution) for solution in solutions))



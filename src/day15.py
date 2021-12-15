"""
ADVENT OF CODE DAY 15 - CHITON
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
    return min(path_lst)


def part2(data):
    """Solve part 2"""
 
def solve(day):
    """Solve the puzzle for the given input"""
    data = parse(day)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

path_lst = []

# SOLUTION FUNCTIONS
def navigate_via_labyrint(labyrint, current_position=(0, 0), total_risk=0, previous_risk=0):
    """
    Navigating through labyrint by recursively calling determine_next_step_in_labyrint method
    and counting the total risk number.
    """
    while current_position:
        try:
            labyrint, next_position, total_risk, previous_risk = determine_next_step_in_labyrint(labyrint, current_position, total_risk, previous_risk)
            return navigate_via_labyrint(labyrint, next_position, total_risk, previous_risk)
        except ValueError:
            break
        except TypeError:
            break



def determine_next_step_in_labyrint(labyrint, current_position, total_risk, previous_risk):
    """
    Determines what is the best next step with follwing rules:
    - only can go to the right or down - means i+1 or row[1][i]
    - if the same numbers are left and row, favor the current moving direction
    """

    risk = None
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
        if right_risk == down_risk:
            new_labyrint = cut_labyrint(labyrint, r, c)
            return navigate_via_labyrint(new_labyrint, right_position, total_risk, previous_risk), navigate_via_labyrint(new_labyrint, down_position, total_risk, previous_risk)
        else:
            next_position, risk = evaluate_next_step_if_both_exist(right_risk, down_risk, right_position, down_position)
    elif not right_risk and not down_risk:
        global path_lst
        if previous_risk == 7:
            path_lst.append(total_risk)
    else:
        next_position, risk = evaluate_next_step_when_border(right_risk, down_risk, right_position, down_position)

    
    if risk:
        total_risk += risk
        return labyrint, next_position, total_risk, risk

def cut_labyrint(labyrint, r, c):
    """Cuts current labyrint to only remanining part."""
    new_labyrint = [row[c:] for row in labyrint[r:]]
    return new_labyrint

def evaluate_next_step_if_both_exist(right_risk, down_risk, right_position, down_position):
    """If both right and left step exists, it determines what next step is better."""

    if right_risk < down_risk:
        return right_position, right_risk    
    elif down_risk < right_risk:
        return down_position, down_risk

def evaluate_next_step_when_border(right_risk, down_risk, right_position, down_position):
    """If there is most right of most down position, or the final step (right down), then it evaluates specifically."""
    if right_risk:
        return right_position, right_risk    
    elif down_risk:
        return down_position, down_risk










if __name__ == "__main__":
    solutions = solve(15)
    print("\n".join(str(solution) for solution in solutions))



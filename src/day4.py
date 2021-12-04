"""
ADVENT OF CODE DAY 4 - GIANT SQUID
Full description: https://adventofcode.com/2021/day/4
"""

# reading input data for the exercise
with open("src/inputs/day4_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

drawing_numbers = [number for number in data[0].split(",")]

boards_raw = data[1:]
boards = []
board = []
for string in boards_raw:
    if len(string) > 1:
        board.append(string.split())
    else:
        boards.append(board)
        board = []

def show_board(board):
        for row in board:
            print(row)

win_board = None

def winning_board(board):
    global win_board
    win_row = check_rows(board)
    win_col = check_cols(board)
    if win_row or win_col:
        win_board = True
        return True
    return False

def check_rows(board):
    for row in board:
        if len(set(row)) == 1:
            return True
    return False

def check_cols(board):
    for i in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[i])
        if len(set(column)) == 1:
            return True
    return False

def make_final_score(board, draw_number):
    total = 0
    for row in board:
        for number in row:
            try:
                total += int(number)
            except ValueError:
                pass
    
    print(draw_number)
    print(total)
    full_score = total * int(draw_number)
    print("The winning board here!!!")
    show_board(board)
    print(f"The full score is: {full_score}")

for draw_number in drawing_numbers:
    for board in boards:
        for row in board:
            for number in row:
                if number == draw_number:
                    ind = row.index(number)
                    row[ind] = 'X'
                    if winning_board(board):
                        make_final_score(board, draw_number)
                        break
            if win_board:
                break
        if win_board:
            break

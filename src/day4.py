"""
ADVENT OF CODE DAY 4 - GIANT SQUID
Full description: https://adventofcode.com/2021/day/4
"""

# reading input data for the exercise
with open("src/inputs/day4_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

# general functions
def create_boards(boards_data):
    """Raw input of board data is serialized and returns formated boards (row = list) in boards list"""
    boards = []
    board = []

    for elem in boards_data:
        row = elem.split()
        if len(row) > 1:
            board.append(row)
            if elem == boards_data[-1]:
                boards.append(board)
        else:
            if board:
                boards.append(board)
                board =[]
    return boards

drawing_numbers = [number for number in data[0].split(",")]
boards_raw = data[1:]
boards = create_boards(boards_raw)

def show_board(board):
    """Shows board in formated output"""
    print()
    for row in board:
        print(row)

first_winning_board = False
last_winning_board = False

def winning_board(board):
    """Checks particular board for win - if at least one row or one col is full of X, returns True"""
    win_row = check_rows(board)
    win_col = check_cols(board)
    if win_row or win_col:
        return True
    return False

def check_rows(board):
    """Check all rows for particular board and returns True if at least one row is full of X"""
    for row in board:
        if len(set(row)) == 1:
            return True
    return False

def check_cols(board):
    """Checks all columns in specific row and returns True if at least one columnn is full of X"""
    for i in range(len(board[0])):
        column = []
        for row in board:
            column.append(row[i])
        if len(set(column)) == 1:
            return True
    return False

def make_final_score(board, draw_number):
    """Count final score and based on first or last announce win"""
    global last_winning_board
    total = 0
    for row in board:
        for number in row:
            try:
                total += int(number)
            except ValueError:
                pass
        
    position = "FIRST" if not last_winning_board else "LAST"
    full_score = total * int(draw_number)
    print(f"\nThe {position} winning board won by number {draw_number}!!!")
    show_board(board)
    print(f"The full score is: {full_score}")

def delete_board_from_boards(index_of_current_board):
    """Deletes boards from the boards list"""
    del boards[index_of_current_board]

def work_with_winning_board(board, draw_number):
    """In case the board wins, following action take place: announce win if it is first, delete from boards list and announce win if it is last"""
    global first_winning_board
    global last_winning_board
    index_of_current_board = boards.index(board)

    if not first_winning_board:
        make_final_score(board, draw_number)
        first_winning_board = True
    # once the board is winning board, it can be deleted from list of boards
    if len(boards) > 1:
        delete_board_from_boards(index_of_current_board)
    if len(boards) == 1: # I have absolutely no clue why else statement is not working but straight coparison is
        last_winning_board = True
        make_final_score(board, draw_number)
        delete_board_from_boards(index_of_current_board)

def verify_draw_number_against_boards(draw_number, boards):
    """Takes current draw number and verify it against all remaining boards. If the number means winning number for the boards, winning board handler take place"""
    for board in boards:
        for row in board:
            for number in row:
                if number == draw_number:
                    ind = row.index(number)
                    row[ind] = 'X'
                    if winning_board(board):
                        work_with_winning_board(board, draw_number)
            if last_winning_board:
                break
        if last_winning_board:
            break

# PART I. + II.
for draw_number in drawing_numbers:
    verify_draw_number_against_boards(draw_number, boards)
    
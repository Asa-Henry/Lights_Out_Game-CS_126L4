# Contributor(s) Name(s): Asa Henry, 
# Contributor(s) Email(s): ajh728@gmail.com, 

# Imports
import random

# Main
def main():
    # Setup
    board = [[' '] * 5 for i in range(5)]
    number_of_moves = 0

    off = '\N{BLACK SQUARE}'
    on = '\N{WHITE SQUARE}'
    states = {'on': on, 'off': off}

    game_Over = False

    board = randomize_board(board, states)


    # Game
    Game(board, number_of_moves, states, game_Over)



# Functions
def randomize_board(board, states):
    for row in range(5):
        for col in range(5):
            state = states[random.choice(list(states))]
            if state == states['on']:
                board[row][col] = states['off']
            else:
                board[row][col] = states['on']

    return board


def Game(board, number_of_moves, states, game_Over):
    while not game_Over:
        display_board(board)
        
        chosen_row = int(input("Please choose a row number (0 - 4): "))
        chosen_col = int(input("Please choose a column number (0 - 4): "))
        
        for row in range(5):
            for col in range(5):
                if (row == chosen_row) and (col == chosen_col):
                    if board[row][col] == states['on']:
                        board[row][col] = states['off']
                    else:
                        board[row][col] = states['on']
                if row == chosen_row:
                    if col == (chosen_col - 1):
                        if board[row][col] == states['on']:
                            board[row][col] = states['off']
                        else:
                            board[row][col] = states['on']
                    elif col == (chosen_col + 1):
                        if board[row][col] == states['on']:
                            board[row][col] = states['off']
                        else:
                            board[row][col] = states['on']
                if col == chosen_col:
                    if row == (chosen_row - 1):
                        if board[row][col] == states['on']:
                            board[row][col] = states['off']
                        else:
                            board[row][col] = states['on']
                    elif row == (chosen_row + 1):
                        if board[row][col] == states['on']:
                            board[row][col] = states['off']
                        else:
                            board[row][col] = states['on']
        

        offs = 0
        for row in range(5):
            for col in range(5):
                if board[row][col] == states['off']:
                    offs += 1

        if offs == 25:
            print(f"Congratulations! You won in {number_of_moves}.")
            game_Over = True
        else:
            number_of_moves += 1


def display_board(board):
    for row in board:
        print(row)




main()


























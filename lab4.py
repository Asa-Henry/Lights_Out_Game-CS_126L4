##################################################################
# CS 126 Lab 4: Lights Off                                       #
# Due: 10/14/2020                                                #
# Asa Henry [ajh728@nau.edu] and Hunter Browning [hsb55@nau.edu] #
##################################################################

# Imports
import random




# Main
def main():
    # Setup
    off = '\N{WHITE SQUARE}'
    on = '\N{BLACK SQUARE}'
    states = {'on': on, 'off': off}

    board = [[off] * 5 for i in range(5)]

    number_of_moves = 0


    game_Over = False

    board = randomize_board(board, states)




    # Game
    Game(board, number_of_moves, states, game_Over)




# Functions
# Setup Functions
def randomize_board(board, states):
    for row in range(5):
        for col in range(5):
            state = states[random.choice(list(states))]

            board[row][col] = state

            if state == states['on']:
                current_row = row
                current_col = col

                board = change_neighbors(current_row, current_col, board, states)

    return board


def change_neighbors(current_row, current_col, board, states):
    if not current_row == 0:
        # Above
        board[current_row - 1][current_col] = change_state(board[current_row - 1][current_col], states)
    
    if not current_col == 0:
        # Left
        board[current_row][current_col - 1] = change_state(board[current_row][current_col - 1], states)

    if not current_col == 4:
        # Right      
        board[current_row][current_col + 1] = change_state(board[current_row][current_col + 1], states)

    if not current_row == 4:
        # Below
        board[current_row + 1][current_col] = change_state(board[current_row + 1][current_col], states)
    
    return board



# Game Functions
def Game(board, number_of_moves, states, game_Over):
    while not game_Over:
        display_board(board)
        

        chosen_row = int(input("Please choose a row number (Please, only 0 - 4): "))
        chosen_col = int(input("Please choose a column number (Please, only 0 - 4): "))


        for row in range(5):
            for col in range(5):
                if (row == chosen_row) and (col == chosen_col):
                    board[row][col] = change_state(board[row][col], states)
                if row == chosen_row:
                    if col == (chosen_col - 1):
                        board[row][col] = change_state(board[row][col], states)
                    elif col == (chosen_col + 1):
                        board[row][col] = change_state(board[row][col], states)
                if col == chosen_col:
                    if row == (chosen_row - 1):
                        board[row][col] = change_state(board[row][col], states)
                    elif row == (chosen_row + 1):
                        board[row][col] = change_state(board[row][col], states)
        

        offs = 0
        for row in range(5):
            for col in range(5):
                if board[row][col] == states['off']:
                    offs += 1

        if offs == 25:
            print('Final board: ')
            display_board(board)
            print(f"Congratulations! You won in {number_of_moves} moves (plus 1).")
            game_Over = True
        else:
            number_of_moves += 1


def change_state(light, states):
    if light == states['on']:
        light = states['off']
    else:
        light = states['on']

    return light


def display_board(board):
    for row in board:
        print(row)




# Calls
main()












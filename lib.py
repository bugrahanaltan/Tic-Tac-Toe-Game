# Created by Bugrahan Altan
import random

# Print the board
def display_board(board):
    print("|", board[7], "|", board[8], "|", board[9], "|")
    print("----------")
    print("|", board[4], "|", board[5], "|", board[6], "|")
    print("----------")
    print("|", board[1], "|", board[2], "|", board[3], "|")

# Take in player input
def player_input():
    choice = ' '
    correct_range = False

    while choice.isdigit() == False or correct_range == False:
        choice = input("Choose a number (1-9): ")
        if choice.isdigit() == False:
            print("Sorry,the input is not an integer. Please try again")

        if choice.isdigit() == True:
            if int(choice) not in range(1, 10):
                print("Sorry, the input is not in the correct range")

            else:
                correct_range = True

    return int(choice)

# Place the inputs on the board
def place_marker(board, marker,position):
     board[position]=marker
     return board

# Check the game if someone won
def win_check(board, mark):
    winning_combinations = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
        [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
        [1, 5, 9], [3, 5, 7]  # Diagonals
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == mark:
            return True

    return False

# Decide which player goes first
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player1'
    else:
        return 'Player2'

# Check the space on the board if there is
def space_check(board, position):
    return board[position] == ' '

# Check the board if it is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# To play again 
def replay():

    play = input("Do you want to play again ? (Y/N) : ")
    if play == 'Y':
        return True
    elif play == 'N':
        return False


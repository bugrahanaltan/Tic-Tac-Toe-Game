# Created by Bugrahan Altan
from lib import display_board
from lib import player_input
from lib import place_marker
from lib import win_check
from lib import choose_first
from lib import space_check
from lib import full_board_check
from lib import replay

test_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
the_board= test_board.copy()
display_board(test_board)

while quit:
    quit = True

# Setting the game
    print('Welcome to X-O-X!')
    if  choose_first() == 'player_1':
        player_1 =True
        player_2 = False
        print("Player 1 is : X ")
        print("Player 2 is : O ")
    else:
        player_2 = True
        player_1 = False
        print("Player 1 is : O")
        print("Player 2 is : X ")
    re_choice = False

    while player_1 == True:
        while re_choice == False:
            choice_x = player_input()
            if space_check(test_board,choice_x) == True:
                place_marker(test_board,'X',choice_x)
                re_choice = True
            else:
                print("The place has already been marked! ")
        display_board(test_board)

        if win_check(test_board,'X')== True:
            print("Player 1 Won!! Congratulations! ")
            if replay() == True:
                test_board = the_board.copy()
                break

            elif replay() == False:
                quit = False
                break

        if full_board_check(test_board) == True:
            print("Its draw ! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break


        while re_choice == True:
            choice_o = player_input()
            if space_check(test_board,choice_o) == True:
                place_marker(test_board,'O',choice_o)
                re_choice = False
            else:
                print("The place has already been marked! ")

        display_board(test_board)

        if win_check(test_board,'O') == True:
            print("Player 2 Won!! Congratulations! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break

        if full_board_check(test_board) == True:
            print("The board is tied ! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break

    while player_2 == True:

        while re_choice == False:
            choice_o = player_input()
            if space_check(test_board,choice_o) == True:
                place_marker(test_board,'O',choice_o)
                re_choice = True
            else:
                print("The place has already been marked! ")

        display_board(test_board)

        if win_check(test_board, 'O') == True:
            print("Player 1 Won!! Congratulations! ")
            if replay():
                test_board = the_board.copy()
                break
            else:
                quit = False
                break
        if full_board_check(test_board) == True:
            print("The board is tied ! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break

        while re_choice == True:
            choice_x = player_input()
            if space_check(test_board,choice_x) == True:
                place_marker(test_board,'X',choice_x)
                re_choice = False
            else:
                print("The place has already been marked! ")
        display_board(test_board)

        if win_check(test_board, 'X') == True:
            print("Player 2 Won! Congratulations! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break

        if full_board_check(test_board) == True:
            print("It's draw ! ")
            if replay() == True:
                test_board = the_board.copy()
                break
            else:
                quit = False
                break

print("Good Bye")
# <----------------- Global Variables ------------------>

board =["-","-","-",
        "-","-","-",
        "-","-","-"]

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

game_is_going = True

#who won ?
winner = None

#who is playing
current_player = "X"

def play_game():
    #display initial board

    display_board()

    #game engine
    while game_is_going == True:

        handle_turn(current_player)

        #flip if game ended

        check_if_game_over()

        flip_player()

        if winner =="X" or winner =="O":
            print(winner + " WON!!!")



def handle_turn(player):
    print("Turn to " + player)
    position = input("Choose a position from 1-9 --> ")
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose a position from 1-9 -->")

        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("position already choosen")

    board[position] = player
    display_board()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner
    #check columns
    column_winner = check_columns()

    #check rows
    row_winner = check_rows()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return
def check_columns():
        # set the golbal Variables
        global game_is_going

        #check is any wins in all the rows
        column_1 = board[0] == board[3] == board[6] != "-"
        column_2 = board[1] == board[4] == board[7] != "-"
        column_3 = board[2] == board[5] == board[8] != "-"

        if column_1 or column_2 or column_3:
            game_is_going = False
        #return the winner (X / O)
        if column_1:
            return board[0]
        elif column_2:
            return board[1]
        elif column_3:
            return board[2]


def check_rows():
    # set the golbal Variables
    global game_is_going

    #check is any wins in all the rows
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_going = False
    #return the winner (X / O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_diagonals():
    # set the golbal Variables
    global game_is_going

    #check is any wins in all the rows
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"


    if diagonal_1 or diagonal_2:
        game_is_going = False
    #return the winner (X / O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]

#flip players between X and O
def flip_player():
    #global variable we need
    global current_player
    # if the current player is X it will change it to O
    if current_player == "X":
        current_player ="O"
    elif current_player =="O":
        current_player ="X"


def check_if_tie():
    global game_is_going
    if "-" not in board:
        print("GAME OVER")
        game_is_going = False





play_game()

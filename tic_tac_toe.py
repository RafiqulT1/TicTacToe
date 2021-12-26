# Display tictactoe table
def display_board(board):
    print("         "+"  |"+"   |")
    print("         "+board[7]+" "+"| "+board[8]+" "+"| "+board[9])
    print("         "+"  |"+"   |")
    print("        "+"- - - - - - ")
    print("         "+"  |"+"   |")
    print("         "+board[4]+" "+"| "+board[5]+" "+"| "+board[6])
    print("         "+"  |"+"   |")
    print("        "+"- - - - - - ")
    print("         "+"  |"+"   |")
    print("         "+board[1]+" "+"| "+board[2]+" "+"| "+board[3])
    print("         "+"  |"+"   |")


# Player choses what they want to be "X"/"O"
def player_input():
    choice = "wrong"
    print("Player to go first will be choosen randomly")
    print("Player_1 would you like to be (X or O)?")
    while choice not in ["X", "O"]:
        choice = input().upper()

        if choice not in ["X", "O"]:
            print("Player_1, please choose X or O:")
    return choice

# Assign "X"/"O" to player_1 and player_2
def assign_player(x_o):
    if x_o == "X":
        player_1 = x_o
        player_2 = "O"
        return player_1, player_2
    elif x_o == "O":
        player_1 = x_o
        player_2 = "X"
        return player_1,player_2


# Player chooses position to place "X"/"O" and check position state (Empty/Full)
def index_input(board, player):
    position = "wrong"
    display_board(empty_board)

    while position not in range(1,10):
        print(player + " Choose your position where you would like to place X or O")
        try:
            position = int(input("Enter position between 1 - 9: "))

        except (ValueError, TypeError):
            print(" ")

        if position not in range(0,10):
            print()
            print("Sorry wrong input!")
            return False
        elif position in range(1,10) and board[position] != " ":
            print("Sorry this place is not empty")
            return False
        else:
            return position


# Place "X"/"O" to selected position
def place_marker(board, player_1, player_2, player, position):
    if player == "player_1":
        board[position] = player_1
    elif player == "player_2":
        board[position] = player_2

# Check if player havev won the game or not
def win_check(board, player_1, player_2, player):
    if ((board[7] == player_1 and board[8] == player_1 and board[9] == player_1) or # across the top
    (board[4] == player_1 and board[5] == player_1 and board[6] == player_1) or # across the middle
    (board[1] == player_1 and board[2] == player_1 and board[3] == player_1) or # across the bottom
    (board[7] == player_1 and board[4] == player_1 and board[1] == player_1) or # down the middle
    (board[8] == player_1 and board[5] == player_1 and board[2] == player_1) or # down the middle
    (board[9] == player_1 and board[6] == player_1 and board[3] == player_1) or # down the right side
    (board[3] == player_1 and board[5] == player_1 and board[7] == player_1) or # diagonal
    (board[9] == player_1 and board[5] == player_1 and board[1] == player_1) or # diagonal
    (board[7] == player_2 and board[8] == player_2 and board[9] == player_2) or # across the top
    (board[4] == player_2 and board[5] == player_2 and board[6] == player_2) or # across the middle
    (board[1] == player_2 and board[2] == player_2 and board[3] == player_2) or # across the bottom
    (board[7] == player_2 and board[4] == player_2 and board[1] == player_2) or # down the middle
    (board[8] == player_2 and board[5] == player_2 and board[2] == player_2) or # down the middle
    (board[9] == player_2 and board[6] == player_2 and board[3] == player_2) or # down the right side
    (board[3] == player_2 and board[5] == player_2 and board[7] == player_2) or # diagonal
    (board[9] == player_2 and board[5] == player_2 and board[1] == player_2)):  # diagonal
        print("win")
        return True


# Randomly chooses player for first move
import random
def choose_first():
    if random.randint(0, 1) == 0:
        return 'player_2'
    else:
        return 'player_1'


# Check if the table state (full/Not Full)
def full_board_check(board):
    full = 0
    for i in board:
        if i == "X" or i == "O":
            full = full + 1
            if full == 9:
                return True
    return False


# ask players if they want to play again or not
def replay():
    replay = "wrong"
    print("Ready to play again? Choose Yes or No: ")

    while replay not in ["yes", "no"]:
        replay = input().lower()
    return replay

# ask players if they are ready to play ot not
def ready():
    ready = "wrong"
    print("Are you ready to play?")
    while ready not in ["yes", "no"]:
        ready = input("Please choose Yes or No: ").lower()
    return ready

# switch turns between player_1 and player_2
def switch_turn(player):
    if player == "player_1":
        player = "player_2"
        return player
    elif player == "player_2":
        player = "player_1"
        return player

#-----------------------------------------------


while True:
    print("\n" * 100)
    print('             Welcome to Tic Tac Toe!')
    empty_board = [" "] * 10
    x_o = player_input()
    player_1, player_2 = assign_player(x_o)
    player = choose_first()

    if player == "player_1":
        print("Player_1 will go first.")
    else:
        print("Player_2 will go first.")

    if ready() == "no":
        break
    else:
        while True:
            print("\n" * 100)
            index = index_input(empty_board, player)
            if index in range(1,10):
                place_marker(empty_board, player_1, player_2, player, index)
                player = switch_turn(player)

            if full_board_check(empty_board) == True:
                print("\n" * 100)
                display_board(empty_board)
                print("Draw Game")
                break
            elif win_check(empty_board, player_1, player_2, player) == True:
                print("\n" * 100)
                display_board(empty_board)
                player = switch_turn(player)
                print(player + " Win")
                break

    if replay() == "no":
        break

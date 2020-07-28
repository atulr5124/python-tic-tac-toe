#######-------Layout-------########
# board
# display board
# play game
# handle a turn 
# check win
    # check rows
    # check columns
    #check diagonals
# check tie
# flip player

# ----- gloabl variables------
# Game baord
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# If game is still going
game_still_going = True

# Who Won? or Tie?
winner = None

# Whose turn is it?
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle a single turn of an arbitrary player
def handle_turn(player):
    position = input("Choose a position from 1-9: ")
    position = int(position) - 1
    board[position] = 'X'
    display_board()

def check_rows():
    return

def check_cols():
    return

def check_diags():
    return

def check_for_winner():
    # check rows
    check_rows()
    # check columns
    check_cols()
    #check diagonals
    check_diags()
    return

def check_if_tie():
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def flip_player():
    return

# Play a game of tic-tac-toe
def play_game():
    # Display initial board
    display_board()
    # While game is still going
    while game_still_going:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)
        # Check if the game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()
    # The game has ended
    if winner == 'X' or winner == 'O':
        print('Player '+winner+" won.")
    elif winner == None:
        print('It\'s a tie')
    else:
        print('Unknown condition')
    
play_game()
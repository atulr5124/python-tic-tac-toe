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
    print(player+'\'s turn')
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in [1,2,3,4,5,6,7,8,9]:
            position = input("Invalid input. Please choose a position from 1-9: ")
        position = int(position) - 1
        if board[position] == '-':
            valid = True
        else:
            print('You cannot go there. Please try again.')
    board[position] = player
    display_board()

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-" 
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return an X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return 

def check_cols():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-" 
    if col_1 or col_2 or col_3:
        game_still_going = False
    # return an X or O
    if col_1:
        return board[0]
    elif col_2:
        return board[3]
    elif col_3:
        return board[6]
    return 

def check_diags():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    # return an X or O
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return 

def check_for_winner():
    # setup gloabl variables
    global winner 
    # check rows
    row_winner = check_rows()
    # check columns
    col_winner = check_cols()
    #check diagonals
    diag_winner = check_diags()
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif diag_winner:
        winner = diag_winner
    else:
        # there was no winner
        winner = None
    return

def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False
    return

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
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
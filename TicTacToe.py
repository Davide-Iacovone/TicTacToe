#The list represents the board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
end = False

#This function displays the board on the screen
def board_display():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

#This function checks the game status
def check_win(board):
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        return True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True
    elif board[0] == "X" and board[1] == "X" and board[2] == "X":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        return True
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        return True
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        return True
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        return True
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        return True
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        return True
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        return True
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        return True
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        return True
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        return True
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        return True
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        return True
    else:
        return False


#This function handles the turns ad in-game input
def handle_turn_x(board):
    success = False
    while not success:
        a = int(input())
        if board[a] == "-":
            board[a] = "X"
            success = True
        else:
            print("This spot is occupied! Try again.")

def handle_turn_o(board):
    success = False
    while not success:
        a = int(input())
        if board[a] == "-":
            board[a] = "O"
            success = True
        else:
            print("This spot is occupied! Try again.")

#This function handles all processes in the game
def play_game(end):
    while True:
        board_display()
        handle_turn_o(board)
        end = check_win(board)
        if end:
            print("The O team has won!!!")
            break
        board_display()
        handle_turn_x(board)
        end = check_win(board)
        if end:
            print("The X team has won!!!")
            break

play_game(end)
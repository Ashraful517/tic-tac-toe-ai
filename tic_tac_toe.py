PLAYER = "X"
AI = "O"
EMPTY = ""

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, player):
    if board[row][col] == EMPTY:
        board[row][col] = player
        return True
    return False

def undo_move(board, row, col):
    board[row][col] = EMPTY

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def is_draw(board):
    for row in board:
        if EMPTY in row:
            return False
    return check_winner(board) is None


EMPTY = ' '

# Initialize a 3x3 board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def is_valid_move(board, row, col):
    return board[row][col] == EMPTY

def make_move(board, row, col, player):
    board[row][col] = player

def undo_move(board, row, col):
    board[row][col] = EMPTY

def check_winner(board):
    lines = []
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != EMPTY:
            return line[0]
        
    return None

def is_draw(board):
    return all(cell != EMPTY for row in board for cell in row)
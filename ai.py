import random

from game_logic import PLAYER, AI, EMPTY, check_winner, is_draw, make_move, undo_move

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    eval = minimax(board, depth - 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER
                    eval = minimax(board, depth - 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board, difficulty):
    if difficulty == "easy":
        return limited_minimax_move(board, depth_limit=1)
    elif difficulty == "medium":
        return limited_minimax_move(board, depth_limit=3)
    elif difficulty == "hard":
        return limited_minimax_move(board, depth_limit=9)  # full depth = perfect AI



def limited_minimax_move(board, depth_limit):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                make_move(board, i, j, AI)
                score = limited_minimax(board, 0, False, -float('inf'), float('inf'), depth_limit)
                undo_move(board, i, j)
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move


def limited_minimax(board, depth, is_maximizing, alpha, beta, depth_limit):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == PLAYER:
        return depth - 10
    elif is_draw(board) or depth >= depth_limit:
        return 0
    
    if is_maximizing:
        max_eval = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    make_move(board, i, j, AI)
                    eval = limited_minimax(board, depth + 1, False, alpha, beta, depth_limit)
                    undo_move(board, i , j)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    make_move(board, i, j, PLAYER)
                    eval = limited_minimax(board,depth + 1, True, alpha, beta, depth_limit)
                    undo_move(board,i,j)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
                    
        return min_eval
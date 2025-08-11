

from tic_tac_toe import PLAYER, AI, EMPTY, check_winner, is_draw, make_move, undo_move

# Minimax with Alpha-Beta Pruning and search depth (difficulty level)
def minimax(board, depth, alpha, beta, is_maximizing, max_depth):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == PLAYER:
        return depth - 10
    elif is_draw(board) or depth == max_depth:
        return 0

    if is_maximizing:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    make_move(board, i, j, AI)
                    eval = minimax(board, depth + 1, alpha, beta, False, max_depth)
                    undo_move(board, i, j)
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
                    eval = minimax(board, depth + 1, alpha, beta, True, max_depth)
                    undo_move(board, i, j)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def get_ai_move(board, difficulty):
    # Difficulty maps to max depth
    depth_map = {
        "Easy": 1,
        "Medium": 3,
        "Hard": 9  # Full depth for unbeatable AI
    }
    max_depth = depth_map[difficulty]
    best_score = float('-inf')
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                make_move(board, i, j, AI)
                score = minimax(board, 0, float('-inf'), float('inf'), False, max_depth)
                undo_move(board, i, j)
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

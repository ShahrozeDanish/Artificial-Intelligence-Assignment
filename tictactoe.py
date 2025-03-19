"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    # Count the number of X's and O's
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)

    # If X has played more, it's O's turn; otherwise, it's X's turn.
    if x_count > o_count:
        return O
    else:
        return X



def actions(board):
    # Find all empty spots
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions_set.add((i, j))
    return actions_set



import copy

def result(board, action):
    # Make a deep copy of the board
    new_board = copy.deepcopy(board)

    # Get the player who’s making the move
    current_player = player(board)

    # Apply the move
    i, j = action
    new_board[i][j] = current_player

    return new_board



def winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]

    # No winner
    return None



def terminal(board):
    # Check for a winner or a full board
    if winner(board) is not None or all(board[i][j] is not EMPTY for i in range(3) for j in range(3)):
        return True
    return False



def utility(board):
    winner_value = winner(board)
    if winner_value == X:
        return 1
    elif winner_value == O:
        return -1
    else:
        return 0



def minimax(board):
    # If the game is over, return None
    if terminal(board):
        return None

    # If it's X's turn (maximizing player)
    if player(board) == X:
        best_val = -math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = min_value(new_board)  # calls the min_value function
            if value > best_val:
                best_val = value
                best_move = action
        return best_move

    # If it's O's turn (minimizing player)
    else:
        best_val = math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            value = max_value(new_board)  # calls the max_value function
            if value < best_val:
                best_val = value
                best_move = action
        return best_move

# Helper functions for Minimax (maximizing and minimizing)
def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 3         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    while not board.check_win():
        empty = board.get_empty_squares()
        rnd_move = random.choice(empty)
        board.move(rnd_move[0], rnd_move[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):

    winner = board.check_win()
    current = player
    opponent = provided.switch_player(player)
    sign = 1

    if winner == provided.DRAW:
        return
    elif winner == None:
        return
    elif winner == opponent:
        sign = -1

    dim = board.get_dim()
    for row in range(dim):
         for col in range(dim):
            if board.square(row,col) == provided.EMPTY:
                pass
            elif board.square(row,col) == current:
                scores[row][col] += SCORE_CURRENT*sign
            elif board.square(row,col) == opponent:
                scores[row][col] -= SCORE_OTHER*sign

def get_best_move(board, scores):
    empty = board.get_empty_squares()

    if not empty:
        raise AssertionError("The board is full")

    best_score = 0
    best_move = []
    for row,col in empty:
        if scores[row][col] == best_score:
            best_move.append((row,col))
        elif scores[row][col] > best_score:
            best_move = [(row,col)]
            best_score = scores[row][col]
    return random.choice(best_move)

def mc_move(board, player, trials):
    dim = board.get_dim()
    scores = [[0 for col in range(dim)] for row in range(dim)]
    for _idx in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)

    best_move = get_best_move(board,scores)
    return best_move



# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

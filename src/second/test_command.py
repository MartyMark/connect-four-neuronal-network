import random
import csv
import copy

from model_load_second import ConnectFourModelLoadSecond
from util import get_outcome, split


def test():
    model = ConnectFourModelLoadSecond()

    e_greedy = 0.7

    total_games = 100

    for i in range(0, total_games):
        playing = True
        current_player = -1
        board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]

        current_game = [copy.deepcopy(board)]

        while playing:  # playing will remain true until the game ends. hence we stick in here.
            if random.uniform(0, 1) <= e_greedy:  # if less than epsil_greedy value, pick random square
                choosing = True
                while choosing:
                    c = random.randint(0, 6)
                    for n in range(5, 0, -1):
                        if board[n][c] == 0:
                            choosing = False
                            board[n][c] = current_player
                            current_game.append(copy.deepcopy(board))
                            break
            else:
                best_move = model.predict(current_player, board)

                board[best_move[0]][best_move[1]] = current_player

                current_game.append(copy.deepcopy(board))

            playable = False

            for row in board:
                for value in row:
                    if value == 0:
                        playable = True  # if there's available squares, continue playing elif find square and check

            if not get_outcome(board) == 0:
                playable = False  # unless there is a winner, 1 or -1.

            if not playable:
                playing = False  # this would be a tie, i believe. all squares full, and no winner.

            if current_player == -1:
                current_player = 1
            else:
                current_player = -1

        with open('trainingdata.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')

            for board in current_game:
                writer.writerow([board])


print(" * Test the Model")
test()
print(" * Test finished")

import copy

from flask import Flask
from flask import request
from flask import jsonify

from game import NUM_COLUMNS, EMPTY_VAL, NUM_ROWS, RED_PLAYER_VAL
from model_load import ConnectFourModelLoad

app = Flask(__name__)

model = ConnectFourModelLoad(42)


def get_available_moves(board):
    available_moves = []
    for j in range(NUM_COLUMNS):
        if board[NUM_ROWS - 1][j] == EMPTY_VAL:
            available_moves.append([NUM_ROWS - 1, j])
        else:
            for i in range(NUM_ROWS - 1):
                if board[i][j] == EMPTY_VAL and board[i + 1][j] != EMPTY_VAL:
                    available_moves.append([i, j])
    return available_moves


def get_move(board, player):
    available_moves = get_available_moves(board)

    max_value = 0
    best_move = available_moves[0]
    for availableMove in available_moves:
        board_copy = copy.deepcopy(board)
        board_copy[availableMove[0]][availableMove[1]] = player
        if player == RED_PLAYER_VAL:
            value = model.predict(board_copy, 2)
        else:
            value = model.predict(board_copy, 0)
        if value > max_value:
            max_value = value
            best_move = availableMove
    return best_move


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    player = message['player']

    best_move = get_move(board, player)

    board[best_move[0]][best_move[1]] = player

    return board

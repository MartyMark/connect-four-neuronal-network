import ast

from flask import Flask
from flask import request

from model_load import ConnectFourModelLoad
from player import Player

app = Flask(__name__)

model = ConnectFourModelLoad(42)


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    player_value = int(message['player'])

    board = ast.literal_eval(board)

    player = Player(player_value, 'model', model)

    best_move = player.get_move(board)

    return {"x": best_move[0], "y": best_move[1]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

"""
This Module holds alle API Routes and their Methods.
"""
import ast

from flask import request

from src import create_app
from src.model_load import ConnectFourModelLoad
from src.player import Player

app = create_app()

model = ConnectFourModelLoad(42)


@app.route("/predict", methods=['POST'])
def predict():
    """Returns the next move of the Neural Network."""
    message = request.get_json(force=True)
    board = message['board']
    player_value = int(message['player'])

    board = ast.literal_eval(board)

    player = Player(player_value, 'model', model)

    best_move = player.get_move(board)

    return {"x": best_move[0], "y": best_move[1]}


@app.route("/")
def test():
    return "hey"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

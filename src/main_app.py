from flask import Flask
from flask import request
from flask import jsonify

from game import Game
from player import Player
from game_controller import GameController
from model import ConnectFourModel

RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
GAME_STATE_NOT_ENDED = 2

app = Flask(__name__)


@app.route("/predict", methods=['POST'])
def predict():
    message = request.get_json(force=True)
    board = message['board']
    response = {
        'response': board
    }
    return jsonify(response)


def train():
    first_game = Game()
    red_player = Player(RED_PLAYER_VAL, 'random')
    yellow_player = Player(YELLOW_PLAYER_VAL, 'random')

    game_controller = GameController(first_game, red_player, yellow_player)
    print(" * Playing with both players with random strategies")
    game_controller.simulate_many_games(10)

    # 42 inputs
    # 3 outputs
    # 50 batch size
    # 100 epochs
    model = ConnectFourModel(42, 3, 50, 100)
    model.train(game_controller.get_training_history())

    red_neural_player = Player(RED_PLAYER_VAL, 'model', model)
    yellow_neural_player = Player(YELLOW_PLAYER_VAL, 'model', model)

    second_game = Game()
    game_controller = GameController(second_game, red_player, yellow_neural_player)
    print(" * Playing with yellow player as Neural Network")
    game_controller.simulate_many_games(10)

    third_game = Game()
    game_controller = GameController(third_game, red_neural_player, yellow_player)
    print(" * Playing with red player as Neural Network")
    game_controller.simulate_many_games(10)


print(" * Loading Keras model and Train")
train()
print(" * Training finished")

"""
if __name__ == "__main__":
    get('http://api.open-notify.org/iss-pass.json', {'lat': '45', 'lon': '180'})

    post('https://httpbin.org/post', data={'key': 'value'})

    #put('https://httpbin.org/put', data={'key': 'value'})"""

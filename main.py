from game import Game
from player import  Player
from game_controller import GameController
from model import ConnectFourModel

RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
GAME_STATE_NOT_ENDED = 2

if __name__ == "__main__":
    firstGame = Game()
    redPlayer = Player(RED_PLAYER_VAL, 'random')
    yellowPlayer = Player(YELLOW_PLAYER_VAL, 'random')

    gameController = GameController(firstGame, redPlayer, yellowPlayer)
    print("Playing with both players with random strategies")
    gameController.simulate_many_games(1000)

    # 42 inputs
    # 3 outputs
    # 50 batch size
    # 100 epochs
    model = ConnectFourModel(42, 3, 50, 100)
    model.train(gameController.get_training_history())

    redNeuralPlayer = Player(RED_PLAYER_VAL, 'model', model)
    yellowNeuralPlayer = Player(YELLOW_PLAYER_VAL, 'model', model)

    secondGame = Game()
    gameController = GameController(secondGame, redPlayer, yellowNeuralPlayer)
    print("Playing with yellow player as Neural Network")
    gameController.simulate_many_games(10)

    thirdGame = Game()
    gameController = GameController(thirdGame, redNeuralPlayer, yellowPlayer)
    print("Playing with red player as Neural Network")
    gameController.simulate_many_games(10)
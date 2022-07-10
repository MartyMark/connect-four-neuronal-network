import copy

RED_PLAYER_VAL = -1
YELLOW_PLAYER_VAL = 1
GAME_STATE_NOT_ENDED = 2


class GameController:

    def __init__(self, game, red_player, yellow_player):
        self.game = game
        self.redPlayer = red_player
        self.yellowPlayer = yellow_player
        self.trainingHistory = []

    def simulate_many_games(self, number_of_games):
        red_player_wins = 0
        yellow_player_wins = 0
        draws = 0
        for i in range(number_of_games):
            self.game.reset_board()
            self.play_game()
            if self.game.get_game_result() == RED_PLAYER_VAL:
                red_player_wins = red_player_wins + 1
            elif self.game.get_game_result() == YELLOW_PLAYER_VAL:
                yellow_player_wins = yellow_player_wins + 1
            else:
                draws = draws + 1
        total_wins = red_player_wins + yellow_player_wins + draws
        print('Red Wins: ' + str(int(red_player_wins * 100 / total_wins)) + '%')
        print('Yellow Wins: ' + str(int(yellow_player_wins * 100 / total_wins)) + '%')
        print('Draws: ' + str(int(draws * 100 / total_wins)) + '%')

    def play_game(self):
        player_to_move = self.redPlayer
        while self.game.get_game_result() == GAME_STATE_NOT_ENDED:
            available_moves = self.game.get_available_moves()
            move = player_to_move.get_move(available_moves, self.game.get_board())
            self.game.move(move, player_to_move.get_player())
            if player_to_move == self.redPlayer:
                player_to_move = self.yellowPlayer
            else:
                player_to_move = self.redPlayer

        for historyItem in self.game.get_board_history():
            self.trainingHistory.append((self.game.get_game_result(), copy.deepcopy(historyItem)))

    def get_training_history(self):
        return self.trainingHistory

import csv

from game import RED_PLAYER_VAL, YELLOW_PLAYER_VAL, GAME_STATE_NOT_ENDED
from operation_util import round_half_up


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

        with open('src/trainingdata.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=';')

            last_twenty_percentage = len(self.trainingHistory) / 100 * 20
            last_twenty_percentage = int(round_half_up(last_twenty_percentage))

            for boardHistory in self.trainingHistory[-last_twenty_percentage:]:
                winner = boardHistory[0]
                boards = boardHistory[1]

                for board in boards:
                    writer.writerow([winner, board])

        total_wins = red_player_wins + yellow_player_wins + draws
        print('Red Wins: ' + str(int(red_player_wins * 100 / total_wins)) + '%')
        print('Yellow Wins: ' + str(int(yellow_player_wins * 100 / total_wins)) + '%')
        print('Draws: ' + str(int(draws * 100 / total_wins)) + '%')

    def play_game(self):
        player_to_move = self.redPlayer
        while self.game.get_game_result() == GAME_STATE_NOT_ENDED:
            move = player_to_move.get_move(self.game.get_board())
            self.game.move(move, player_to_move.get_player())
            if player_to_move == self.redPlayer:
                player_to_move = self.yellowPlayer
            else:
                player_to_move = self.redPlayer

        self.trainingHistory.append((self.game.get_game_result(), self.game.get_board_history()))

    def get_training_history(self):
        return self.trainingHistory

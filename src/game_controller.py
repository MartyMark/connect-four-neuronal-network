import csv

from game import RED_PLAYER_VAL, YELLOW_PLAYER_VAL, GAME_STATE_NOT_ENDED


class GameController:

    def __init__(self, game, red_player, yellow_player):
        self.game = game
        self.red_player = red_player
        self.yellow_player = yellow_player
        self.training_history = []

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

        with open('src/trainingdata.csv', 'a', encoding="UTF-8", newline='') as file:
            writer = csv.writer(file, delimiter=';')

            for board_history in self.training_history:
                winner = board_history[0]
                boards = board_history[1]

                for board in boards:
                    writer.writerow([winner, board])

        total_wins = red_player_wins + yellow_player_wins + draws
        print('Red Wins: ' + str(int(red_player_wins * 100 / total_wins)) + '%')
        print('Yellow Wins: ' + str(int(yellow_player_wins * 100 / total_wins)) + '%')
        print('Draws: ' + str(int(draws * 100 / total_wins)) + '%')

    def play_game(self):
        player_to_move = self.red_player
        while self.game.get_game_result() == GAME_STATE_NOT_ENDED:
            move = player_to_move.get_move(self.game.get_board())
            self.game.move(move, player_to_move.get_player())
            if player_to_move == self.red_player:
                player_to_move = self.yellow_player
            else:
                player_to_move = self.red_player

        self.training_history.append((self.game.get_game_result(), self.game.get_board_history()))

    def get_training_history(self):
        return self.training_history

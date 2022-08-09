import numpy as np
import random
import math
import copy
from keras.layers import Dense
from keras.models import Sequential
from tensorflow import keras

from util import one_hot, get_outcome, one_hot_old


class ConnectFourModelTrainSecond:

    def __init__(self):
        self.model = Sequential()
        self.model.add(Dense(units=130, activation='relu', input_dim=126, kernel_initializer='random_uniform',
                             bias_initializer='zeros'))
        self.model.add(
            Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(
            Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(
            Dense(units=900, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(
            Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(
            Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(
            Dense(units=130, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.add(Dense(7, kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

        self.model_2 = Sequential()
        self.model_2.add(Dense(units=130, activation='relu', input_dim=126, kernel_initializer='random_uniform',
                               bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=900, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(
            Dense(units=130, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.add(Dense(7, kernel_initializer='random_uniform', bias_initializer='zeros'))
        self.model_2.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

    def train(self, games):
        reward_dep = .7
        xt = 0  # initialise X, O and drawn wins
        ot = 0
        dt = 0
        states = []
        q_values = []
        states_2 = []
        q_values_2 = []

        for game in games:  # game is the full game history from all empty squares, to the finished game state. games is a list of all these game histories.
            total_reward = get_outcome(game[len(game) - 1])  # minus 1 because length is magnitude starting at 1 whereas information starts at 0. So this line gets the final result of the game
            if total_reward == -1:  ## these lines add to the sum of scores for this set of 2000 games
                ot += 1
            elif total_reward == 1:
                xt += 1
            else:
                dt += 1

            for i in range(1, len(game)):

                last_board = game[i-1][0] + game[i-1][1] + game[i-1][2] + game[i-1][3] + game[i-1][4] + game[i-1][5]

                board = game[i][0] + game[i][1] + game[i][2] + game[i][3] + game[i][4] + game[i][5]

                if i % 2 == 1:  # this shows if it was X's turn???
                    for j in range(0, 42):
                        if not last_board[j] == board[j]:  # #i is the gamestate history leading up to the final
                            # gamestate. j is the individual squares in the game histories. so this is comparing
                            # individual squares and seeing if they changed
                            reward_vector = np.zeros(7)  # return an array of a given shape filled with zeros.

                            # this exponent returns values between 0 and 4, based on game length. if you're in the
                            # won gamestate, total reward == reward vector == 0 or 1 or -1
                            reward_vector[j % 7] = total_reward * (
                                    reward_dep ** (math.floor((len(game) - (i - 1)) / 2) - 1))
                            # the further you are away from finishing the game, the reward_dep(th?) factor diminishes
                            # the reward value of a winning state. if a states becomes winning for X, but you are on
                            # move 1, making that move has a low value. Making the final winning move is high value.
                            states.append(copy.deepcopy(board))  # add each specific game state to the states list.
                            q_values.append(copy.deepcopy(reward_vector))  # add each reward vector to the q values list.
                            # print(game[i])
                            # print(reward_vector)

                else:
                    for j in range(0, 42):
                        if not last_board[j] == board[j]:  # copy for O's(?)
                            reward_vector = np.zeros(7)
                            reward_vector[j % 7] = -1 * total_reward * (
                                    reward_dep ** (math.floor((len(game) - (i - 1)) / 2) - 1))
                            states_2.append(copy.deepcopy(board))
                            q_values_2.append(copy.deepcopy(reward_vector))

        zipped = list(zip(states, q_values))
        random.shuffle(zipped)
        states, q_values = zip(*zipped)  # the '*' is used to unzip the list.
        new_states = []
        for state in states:  # this takes a random game state, converts it into binary 27 length list, and adds
            # to new state
            new_states.append(one_hot_old(state))

        self.model.fit(np.asarray(new_states), np.asarray(q_values), epochs=4, batch_size=len(q_values), verbose=1)

        zipped_2 = list(zip(states_2, q_values_2))
        random.shuffle(zipped_2)
        states_2, q_values_2 = zip(*zipped_2)
        new_states_2 = []
        for state in states_2:
            new_states_2.append(one_hot_old(state))

        self.model_2.fit(np.asarray(new_states_2), np.asarray(q_values_2), epochs=4, batch_size=len(q_values_2), verbose=1)

    def save(self):
        self.model.save('nn_model_second')
        self.model_2.save('nn_model_2_second')
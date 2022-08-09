import math
import random
import time

import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from keras.models import load_model

reward_dep = .7
x_train = True

model = Sequential()
model.add(Dense(units=130, activation='relu', input_dim=126, kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=900, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(units=130, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model.add(Dense(7, kernel_initializer='random_uniform', bias_initializer='zeros'))
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])

model_2 = Sequential()
model_2.add(Dense(units=130, activation='relu', input_dim=126, kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=900, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=600, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=250, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(units=130, activation='relu', kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.add(Dense(7, kernel_initializer='random_uniform', bias_initializer='zeros'))
model_2.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])


def one_hot(state):
    current_state = []

    for square in state:  # state is a list of the squares, square is an indiv square. 0 = empty. 1 = X. -1 = O.
        if square == 0:
            current_state.append(1)
            current_state.append(0)
            current_state.append(0)
        elif square == 1:
            current_state.append(0)
            current_state.append(1)
            current_state.append(0)
        elif square == -1:
            current_state.append(0)
            current_state.append(0)
            current_state.append(1)  # this code converts a 3x3 grid with values, (or a list of 9 locations as it's
            # treated here) into a list of 27 values.
            # empty = 000, X = 010, O = 001.

    return current_state


def get_outcome(state):
    total_reward = 0

    # for i in range(0, 9): if i == 0 or i == 3 or i == 6: # start in a left hand cell, if the follow 2 cells match,
    # reward = 1 or -1 or 0. if state[i] == state[i + 1] and state[i] == state[i + 2]: total_reward = state[i] break
    # elif state[0] == state[4] and state[0] == state[8] and i == 0: #dia line top left corner to bottom right.
    # total_reward = state[0] break if i < 3: if state[i] == state[i + 3] and state[i] == state[i + 6]: total_reward
    # = state[i] break elif state[2] == state[4] and state[2] == state[6] and i == 2: total_reward = state[2] break

    # if (state[0] == state[1] == state[2]) and not state[0] == 0: ##superceding if statements for the 8 possible lines.
    #     total_reward = state[0]
    # elif (state[3] == state[4] == state[5]) and not state[3] == 0:
    #     total_reward = state[3]
    # elif (state[6] == state[7] == state[8]) and not state[6] == 0:
    #     total_reward = state[6]
    # elif (state[0] == state[3] == state[6]) and not state[0] == 0:
    #     total_reward = state[0]
    # elif (state[1] == state[4] == state[7]) and not state[1] == 0:
    #     total_reward = state[1]
    # elif (state[2] == state[5] == state[8]) and not state[2] == 0:
    #     total_reward = state[2]
    # elif (state[0] == state[4] == state[8]) and not state[0] == 0:
    #     total_reward = state[0]
    # elif (state[2] == state[4] == state[6]) and not state[2] == 0:
    #     total_reward = state[2]

    for y in range(0, 35 + 1, 7):  # check for horizontal four in a row
        for x in range(y, y + 4):
            if state[x] == state[x + 1] == state[x + 2] == state[x + 3] and not state[x] == 0:
                total_reward = state[x]

    for x in range(0, 7):  # check for vertical four in a row
        for y in range(x, x + (3 * 7), 7):
            if state[y] == state[y + 7] == state[y + 14] == state[y + 21] and not state[y] == 0:
                total_reward = state[y]

    for x in range(0, 21, 7):  # check for downwards right diagonal
        for y in range(x, x + 4, 1):
            if state[y] == state[y + 8] == state[y + 16] == state[y + 24] and not state[y] == 0:
                total_reward = state[y]

    for x in range(3, 24, 7):  # check for upwards right diagonal
        for y in range(x, x + 4, 1):
            if state[y] == state[y + 6] == state[y + 12] == state[y + 18] and not state[y] == 0:
                total_reward = state[y]

    return total_reward


try:
    model = load_model('../test/connect_four_deep.h5')
    model_2 = load_model('../test/connect_four_2_deep.h5')
    print('Pre-existing model found... loading data.')
except:
    pass


def process_games(games, model, model_2):
    global x_train  # taken from the x_train outside of the function
    xt = 0  # initialise X, O and drawn wins
    ot = 0
    dt = 0
    states = []
    q_values = []
    states_2 = []
    q_values_2 = []

    for game in games:  # game is the full game history from all empty squares, to the finished game state. games is a list of all these game histories.
        total_reward = get_outcome(game[
                                       len(game) - 1])  # minus 1 because length is magnitude starting at 1 whereas information starts at 0. So this line gets the final result of the game
        if total_reward == -1:  ## these lines add to the sum of scores for this set of 2000 games
            ot += 1
        elif total_reward == 1:
            xt += 1
        else:
            dt += 1
        # print('------------------')
        # print(game[len(game) - 1][0], game[len(game) - 1][1], game[len(game) - 1][2])
        # print(game[len(game) - 1][3], game[len(game) - 1][4], game[len(game) - 1][5])
        # print(game[len(game) - 1][6], game[len(game) - 1][7], game[len(game) - 1][8])
        # print('reward =', total_reward)

        for i in range(1, len(game)):
            if i % 2 == 1:  # this shows if it was X's turn???
                for j in range(0, 42):
                    if not game[i - 1][j] == game[i][
                        j]:  ##i is the gamestate history leading up to the final gamestate. j is the individual squares in the game histories. so this is comparing individual squares and seeing if they changed
                        reward_vector = np.zeros(7)  # return an array of a given shape filled with zeros.
                        reward_vector[j % 7] = total_reward * (reward_dep ** (math.floor((len(game) - (
                                i - 1)) / 2) - 1))  # this exponent returns values between 0 and 4, based on game length. if you're in the won gamestate, total reward == reward vector == 0 or 1 or -1
                        # the further you are away from finishing the game, the reward_dep(th?) factor diminishes the reward value of a winning state. if a states becomes winning for X, but you are on move 1, making that move has a low value. Making the final winning move is high value.
                        states.append(game[i].copy())  ##add each specific game state to the states list.
                        q_values.append(reward_vector.copy())  # add each reward vector to the q values list.
                        # print(game[i])
                        # print(reward_vector)

            else:
                for j in range(0, 42):
                    if not game[i - 1][j] == game[i][j]:  ##copy for O's(?)
                        reward_vector = np.zeros(7)
                        reward_vector[j % 7] = -1 * total_reward * (
                                reward_dep ** (math.floor((len(game) - (i - 1)) / 2) - 1))
                        states_2.append(game[i].copy())
                        q_values_2.append(reward_vector.copy())
                        # print(game[i])
                        # print(reward_vector)

    if x_train:
        zipped = list(zip(states, q_values))
        random.shuffle(zipped)
        states, q_values = zip(*zipped)  # the '*' is used to unzip the list.
        new_states = []
        for state in states:  # this takes a random game state, converts it into binary 27 length list, and adds to new state
            new_states.append(one_hot(state))

        # for i in range(0, len(states)):
        # print(new_states[i], states[i], q_values[i])
        # print(np.asarray(new_states))

        model.fit(np.asarray(new_states), np.asarray(q_values), epochs=4, batch_size=len(q_values), verbose=1)
        model.save('connect_four_deep.h5')
        del model
        model = load_model('../test/connect_four_deep.h5')
        print(xt / 20, ot / 20, dt / 20)  # these are %s of Xwin, O win, draw, in training.
        print(len(games))
    else:
        zipped = list(zip(states_2, q_values_2))
        random.shuffle(zipped)
        states_2, q_values_2 = zip(*zipped)
        new_states = []
        for state in states_2:
            new_states.append(one_hot(state))

        # for i in range(0, len(states)):
        # print(new_states[i], states[i], q_values[i])
        # print(np.asarray(new_states))

        model_2.fit(np.asarray(new_states), np.asarray(q_values_2), epochs=4, batch_size=len(q_values_2), verbose=1)
        model_2.save('connect_four_2_deep.h5')
        del model_2
        model_2 = load_model('../test/connect_four_2_deep.h5')
        print(xt / 20, ot / 20, dt / 20)

    x_train = not x_train  # this basically just alternates x_train from True to False to True.


# win = 1; draw = 0; loss = -1 --> moves not taken are 0 in q vector


# mode = input('Choose a mode: (training/playing) ')
mode = 'training'

games_played = 0
start_time = time.time()
e_greedy = 0.95

while True:  # this is basically the main function inside a while true loop
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0]
    # sides --> 0 = Os, 1 = Xs
    games = []
    current_game = []

    if mode == 'training':
        print(x_train)
        # total_games = int(input('How many games should be played? '))
        total_games = 3
        # e_greedy = float(input('What will the epsilon-greedy value be? '))

        for i in range(0, total_games):
            playing = True
            nn_turn = True
            c = 0  # used later for choosing a random square
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0]
            # sides --> 0 = Os, 1 = Xs
            current_game = [board.copy()]
            nn_board = board

            while playing:  # playing will remain true until the game ends. hence we stick in here.
                if nn_turn:
                    if random.uniform(0, 1) <= e_greedy:  # if less than epsil_greedy value, pick random square
                        choosing = True
                        while choosing:
                            c = random.randint(0, 6)  # options are 0 to 6, this function is inclusive.
                            for y in range(35, -1, -7):
                                if board[c + y] == 0:  # if square is empty, make it 1.
                                    choosing = False
                                    board[c + y] = 1
                                    current_game.append(board.copy())
                                    break
                            # save state to game array
                    else:  # else take model prediction. Interesting as it's random 70% of the time. Explains why so
                        # many wins/losses in training.
                        pre = model.predict(np.asarray([one_hot(board)]), batch_size=1)[0]  # converts current board state into the 27 length binary game state.
                        # [0] because the model comes out like [[]] so we want to remove one set of square brackets.
                        highest = -1000
                        num = -1
                        for j in range(0, 7):
                            if board[j] == 0:  # if square is empty, check prediction for that move. keep highest
                                # scoring move.
                                if pre[j] > highest:
                                    highest = pre[j].copy()
                                    num = j

                        choosing = False
                        for y in range(35, -1, -7):
                            if board[num + y] == 0:  # if square is empty, make it 1.
                                board[num + y] = 1
                                break
                        current_game.append(board.copy())

                else:
                    if random.uniform(0, 1) <= e_greedy:
                        choosing = True
                        while choosing:
                            c = random.randint(0, 6)
                            for y in range(35, -1, -7):
                                if board[c + y] == 0:  # if square is empty, make it 1.
                                    choosing = False
                                    board[c + y] = -1
                                    current_game.append(board.copy())
                                    break
                            # save state to game array
                    else:
                        pre = model_2.predict(np.asarray([one_hot(board)]), batch_size=1)[0]

                        highest = -1000
                        num = -1
                        for j in range(0, 7):
                            if board[j] == 0:
                                if pre[j] > highest:
                                    highest = pre[j].copy()
                                    num = j

                        choosing = False
                        for y in range(35, -1, -7):
                            if board[num + y] == 0:  # if square is empty, make it 1.
                                board[num + y] = -1
                                break
                        current_game.append(board.copy())

                playable = False

                for square in board:
                    if square == 0:
                        playable = True  # if there's available squares, continue playing
                # elif find square and check

                if not get_outcome(board) == 0:
                    playable = False  # unless there is a winner, 1 or -1.

                # print(get_outcome(board))

                if not playable:
                    playing = False  # this would be a tie, i believe. all squares full, and no winner.

                nn_turn = not nn_turn  # flip turn over. True = X turn. False = O turn

            # print(board[0], board[1], board[2])
            # print(board[3], board[4], board[5])
            # print(board[6], board[7], board[8])

            games.append(current_game)  # add this game to games

        r_board = []

        for square in board:  # board for printing
            if square == 0:
                r_board.append('-')
            elif square == 1:
                r_board.append('x')
            elif square == -1:
                r_board.append('o')

        for x in range(0, 42, 7):
            print(r_board[x], r_board[x + 1], r_board[x + 2], r_board[x + 3], r_board[x + 4], r_board[x + 5],
                  r_board[x + 6])

        # for x in range(0, 42, 7):
        #     print(board[x], board[x + 1], board[x + 2], board[x + 3], board[x + 4], board[x + 5],
        #           board[x + 6])

        # print('current game:', current_game)

        process_games(games, model, model_2)

        games_played += 2000
        # if games_played % 4000 == 0:
        #   quit()
        print(e_greedy, games_played, (time.time() - start_time) / 60)
    elif mode == 'playing':
        print('')
        print('A new game is starting!')
        print('')

        team = input('Choose a side: (x/o) ')
        print('')

        board = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0]
        running = True
        x_turn = True
        while running:
            if (x_turn and team == 'o') or (
                    not x_turn and not team == 'o'):  ##if it's x turn and human is O, AI move. if O turn and team is X, AI move.
                if team == 'o':
                    pre = model.predict(np.asarray([one_hot(board)]), batch_size=1)[0]
                elif team == 'x':
                    pre = model_2.predict(np.asarray([one_hot(board)]), batch_size=1)[0]
                print(pre)
                print('')
                highest = -1000
                num = -1
                for j in range(0, 7):
                    if board[j] == 0:
                        if pre[j] > highest:
                            highest = pre[j].copy()
                            num = j

                # TODO: ADD EXTRA IF STATEMENT FOR NUM == -1 (FIRST OPTION ALWAYS TRUMPS)

                if team == 'o':
                    for y in range(35, -1, -7):
                        if board[num + y] == 0:  # if square is empty, make it 1.
                            board[num + y] = 1
                            break
                elif team == 'x':
                    for y in range(35, -1, -7):
                        if board[num + y] == 0:  # if square is empty, make it 1.
                            board[num + y] = -1
                            break
                x_turn = not x_turn
                print('AI is thinking...')
            else:
                move = int(input('Input your move, 0-->6: '))  ##make human move
                if board[move] == 0:
                    if team == 'o':
                        for y in range(35, -1, -7):
                            if board[move + y] == 0:  # if square is empty, make it 1.
                                board[move + y] = -1
                                break
                    elif team == 'x':
                        for y in range(35, -1, -7):
                            if board[move + y] == 0:  # if square is empty, make it 1.
                                board[move + y] = 1
                                break
                    x_turn = not x_turn
                else:
                    print('Invalid move!')

            r_board = []

            for square in board:  # board for printing
                if square == 0:
                    r_board.append('-')
                elif square == 1:
                    r_board.append('x')
                elif square == -1:
                    r_board.append('o')

            for x in range(0, 42, 7):
                print(r_board[x], r_board[x + 1], r_board[x + 2], r_board[x + 3], r_board[x + 4], r_board[x + 5],
                      r_board[x + 6])

            full = True

            for square in board:
                if square == 0:
                    full = False

            if full:
                running = False
                if get_outcome(board) == 0:
                    print('The game was drawn!')

            if not get_outcome(board) == 0:
                running = False
                print(get_outcome(board), 'won the game!')
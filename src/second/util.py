def one_hot_old(state):
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


def one_hot(state):
    state = state[0] + state[1] + state[2] + state[3] + state[4] + state[5]

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
    state = state[0] + state[1] + state[2] + state[3] + state[4] + state[5]

    total_reward = 0

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


def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

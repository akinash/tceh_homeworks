# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random
import copy


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """

    field = list(range(1,16))
    field.append(EMPTY_MARK)
    random.shuffle(field)
    field = [field[x:x + 4] for x in range(0, len(field), 4)]

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """

    print('\n'.join([''.join(['{:4}'.format(str(item)) for item in row])
                     for row in field]))
    print('---------------')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """

    win_field = list(range(1,16))
    win_field.append(EMPTY_MARK)
    win_field = [win_field[x:x + 4] for x in range(0, len(win_field), 4)]

    return field == win_field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    current_coord = {'x':4, 'y':4}
    for y_coord, y_value in enumerate(field):
        for x_coord, x_value in enumerate(y_value):
            if x_value == 'x':
                current_coord = {'x':x_coord, 'y':y_coord}
                break

    if key == "w":
        new_coord = {'x': current_coord['x'], 'y': current_coord['y'] - 1}
    elif key == "a":
        new_coord = {'x': current_coord['x'] - 1, 'y': current_coord['y']}
    elif key == "s":
        new_coord = {'x': current_coord['x'], 'y': current_coord['y'] + 1}
    else:
        new_coord = {'x': current_coord['x'] + 1, 'y': current_coord['y']}

    if new_coord['x'] > 3 or new_coord['y'] > 3 or new_coord['x'] < 0 or new_coord['y'] < 0:
        raise IndexError

    field[current_coord['y']][current_coord['x']] = field[new_coord['y']][new_coord['x']]
    field[new_coord['y']][new_coord['x']] = 'x'

    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """

    keys = MOVES.keys()

    user_input = input('Ваш ход: ')
    if user_input not in keys:
        raise ValueError

    return user_input



def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """

    field = shuffle_field()

    print_field(field)

    while True:
        try:
            user_input = handle_user_input()
        except ValueError:
            print('Допустимы только {}'.format(' '.join(list(MOVES.keys()))))
            continue

        try:
            field = perform_move(field, user_input)
        except IndexError:
            print('Так ходить нельзя')
            continue

        print_field(field)

        if is_game_finished(field):
            break

    print('Игра окончена!')


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()

# -*- coding:utf-8 -*-

"""Game engine."""

from sys import exit

import prompt

ROUNDS_COUNT = 3


def engine(game):
    """
    Game engine.

    Parameters:
        game: module of the game

    Returns: None
    """
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_user))
    print(game.GAME_RULE)

    for _ in range(ROUNDS_COUNT):
        task, correct_answer = game.get_task_and_solution()
        print('Question: {0}'.format(task))
        answer_user = get_correct_answer_user(game)
        if answer_user == correct_answer:
            print('Correct!')
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    else:
        print('Congratulations, {0}!'.format(name_user))


def get_correct_answer_user(game):
    """
    Get the correct user respons.

    Parameters:
        game: module of the game

    Returns:
        str or int
    """
    tries_count = 3
    game_name = game.__name__.rsplit('.')[-1]

    for _ in range(tries_count):
        answer_user = prompt.string('Your answer: ')
        if game_name in {'calc', 'gcd', 'progression'}:
            try:
                return int(answer_user)
            except ValueError:
                print('{0} - invalid data, enter an integer.'.format(
                    answer_user,
                ))
                continue
        if game_name in {'even', 'prime'} and answer_user in {'yes', 'no'}:
            return answer_user
        else:
            print('{0} - invalid data, enter an "yes" or "no".'.format(
                answer_user,
            ))
            continue

    exit('Attempts ended. Start the game again.')


def show_game_over(answer_user, correct_answer, name_user):
    """
    Show that the user's answer is incorrect and offers to play again.

    Parameters:
        answer_user: str or int
        correct_answer: str or int
        name_user: str

    Returns: None
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
        answer_user,
        correct_answer,
    ))
    print("Let's try again, {0}!".format(name_user))

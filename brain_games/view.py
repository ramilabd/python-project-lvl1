# -*- coding:utf-8 -*-

"""The module of user interaction."""

from sys import exit

import prompt


def show_rules_game(game_module):
    """
    Show the rules of the game.

    Parameters:
        game_module: module of the game

    Returns: None
    """
    print(game_module.GAME_RULE)


def show_task(task):
    """
    Show question.

    Parameters:
        task: str

    Returns: None
    """
    print('Question: {0}'.format(task))


def get_correct_answer_user(game_module, tries=3):
    """
    Get the correct user respons.

    Parameters:
        game_module: module of the game
        tries: int

    Returns:
        str or int
    """
    if tries == 0:
        exit('Attempts ended. Start the game again.')

    answer_user = prompt.string('Your answer: ')
    game_name = game_module.__name__.rsplit('.')[-1]

    if game_name in {'calc', 'gcd', 'progression'}:
        try:
            return int(answer_user)
        except ValueError:
            print('{0} - invalid data, enter an integer.'.format(
                answer_user,
            ))
            get_correct_answer_user(game_module, tries - 1)

    if game_name in {'even', 'prime'} and answer_user in {'yes', 'no'}:
        return answer_user
    else:
        print('{0} - invalid data, enter an "yes" or "no".'.format(
            answer_user,
        ))
        get_correct_answer_user(game_module, tries - 1)


def confirm_correct_answer(name_user=''):
    """
    Show that the user won.

    Parameters:
        name_user: str (by default == '')

    Returns: None
    """
    if name_user:
        print('Congratulations, {0}!'.format(name_user))
    else:
        print('Correct!')


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

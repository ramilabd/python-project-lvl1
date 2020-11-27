# -*- coding:utf-8 -*-

"""Functions of the game "Brain-even."""

from random import randint

GAME_RULE = 'Answer "yes" if number even otherwise answer "no".'


def generator_task_and_solution():
    """
    Generate an integer in a specific range.

    Parameters are missing.

    Returns:
        tuple
    """
    task = randint(1, 100)
    correct_answer = 'yes' if task % 2 == 0 else 'no'

    return task, correct_answer


def is_correct_data(answer_user):
    """
    Сhecks whether the input data is correct.

    Parameters:
        answer_user: str

    Returns:
        tuple
    """
    if answer_user in {'yes', 'no'}:
        return True, answer_user
    return False, '{0} - invalid data, enter an "yes" or "no".'.format(
        answer_user,
    )

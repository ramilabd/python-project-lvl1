# -*- coding:utf-8 -*-

"""Functions of the game "Brain-prime."""

from random import randint

GAME_RULE = 'Answer "yes" if given number is prime.Otherwise answer "no".'


def is_prime(number):
    """
    Check the number for simplicity.

    Parameters:
        number: int

    Returns:
        bool
    """
    if (number < 2):
        return False

    divider = 2
    max_divider = number // divider

    while divider <= max_divider:
        if number % divider == 0:
            return False
        divider += 1

    return True


def generator_task_and_solution():
    """
    Generate an integer in a specific range.

    Parameters are missing.

    Returns:
        tuple
    """
    task = randint(1, 101)
    correct_answer = 'yes' if is_prime(task) else 'no'

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

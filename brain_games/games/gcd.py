# -*- coding:utf-8 -*-

"""Functions of the game "Brain-gcd."""


from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def generator_task_and_solution():
    """
    Get two numbers and the greatest common divisor.

    Parameters are missing.

    Returns:
        tuple
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = gcd(number1, number2)

    task = ' '.join(map(str, (number1, number2)))
    return task, correct_answer


def is_correct_data(answer_user):
    """
    Сhecks whether the input data is correct.

    Parameters:
        answer_user: str

    Returns:
        tuple
    """
    try:
        return True, int(answer_user)
    except ValueError:
        return False, '{0} - invalid data, enter an integer.'.format(
            answer_user,
        )

# -*- coding:utf-8 -*-

"""Functions of the game "Brain-gcd."""


from math import gcd
from random import randint

GAME_RULE = 'Find the greatest common divisor of given numbers.'


def get_task_and_solution():
    """
    Get two numbers (task) and the greatest common divisor.

    Parameters are missing.

    Returns:
        tuple: (int, str)
    """
    number1 = randint(1, 100)
    number2 = randint(1, 100)
    correct_answer = gcd(number1, number2)
    task = '{0} {1}'.format(number1, number2)

    return task, str(correct_answer)

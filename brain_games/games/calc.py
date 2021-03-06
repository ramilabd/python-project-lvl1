# -*- coding:utf-8 -*-

"""Functions of the game "Brain-calc."""


from operator import add, mul, sub
from random import choice, randint

GAME_RULE = 'What is the result of the expression?'


math_operations = {
    '+': add,
    '-': sub,
    '*': mul,
}


def get_task_and_solution():
    """
    Get a mathematical expression (task) and correct answer.

    Parameters are missing.

    Returns:
        tuple: str
    """
    numbers = randint(1, 10), randint(1, 10)
    math_symbol, math_operation = choice(list(math_operations.items()))

    correct_answer = math_operation(*numbers)
    task = '{1} {0} {2}'.format(math_symbol, *numbers)

    return task, str(correct_answer)

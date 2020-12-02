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


def get_math_operation():
    """
    Get a random mathematical operation.

    Parameters are missing.

    Returns:
        str ('+' or '-' or '*')
    """
    return choice(list(math_operations.keys()))


def get_task_and_solution():
    """
    Get a mathematical expression (task) and correct answer.

    Parameters are missing.

    Returns:
        tuple
    """
    number1 = randint(1, 10)
    number2 = randint(1, 10)
    math_operator = get_math_operation()
    correct_answer = math_operations[math_operator](number1, number2)

    task = ' '.join(map(str, (number1, math_operator, number2)))
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

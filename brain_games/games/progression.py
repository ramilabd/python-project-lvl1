# -*- coding:utf-8 -*-

"""Functions of the game "Brain-progression."""

from operator import add, sub
from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'

START_MIN = 1
START_MAX = 10
STEP_MIN = 1
STEP_MAX = 10
LEN_SEQUENCE = 10


def get_task_and_solution():
    """
    Get a tuple of integers (task) and a hidden number (correct answer).

    Parameters are missing.

    Returns:
        tuple
    """
    sequence = get_arithmetic_progression()

    correct_answer = choice(sequence)
    task = (
        '..' if number == correct_answer else str(number) for number in sequence
    )
    task = ' '.join(task)

    return task, correct_answer


def get_arithmetic_progression():
    """
    Get an arithmetic progression.

    Parameters are missing.

    Returns:
        list
    """
    start = randint(START_MIN, START_MAX)
    step = randint(STEP_MIN, STEP_MAX)
    len_sequence = LEN_SEQUENCE
    sequence = []

    operation = choice([add, sub])

    while len_sequence:
        start = operation(start, step)
        sequence.append(start)
        len_sequence -= 1

    return sequence


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

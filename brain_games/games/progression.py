# -*- coding:utf-8 -*-

"""Functions of the game "Brain-progression."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'
LEN_SEQUENCE = 10


def get_task_and_solution():
    """
    Get a tuple of integers (task) and a hidden number (correct answer).

    Parameters are missing.

    Returns:
        tuple: (str, int)
    """
    start, step = randint(1, 10), randint(1, 10)
    sequence = list(range(start, LEN_SEQUENCE * step + start, step))

    correct_answer = choice(sequence)
    task = ' '.join(
        '..' if number == correct_answer else str(number) for number in sequence
    )

    return task, str(correct_answer)

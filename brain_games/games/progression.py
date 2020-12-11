# -*- coding:utf-8 -*-

"""Functions of the game "Brain-progression."""

from random import choice, randint

GAME_RULE = 'What number is missing in the progression?'


def get_task_and_solution():
    """
    Get a tuple of integers (task) and a hidden number (correct answer).

    Parameters are missing.

    Returns:
        tuple: (str, int)
    """
    start = randint(1, 10)
    step = randint(1, 10)
    len_sequence = 10
    max_value_item = len_sequence * step + start

    sequence = [number for number in range(start, max_value_item, step)]

    correct_answer = choice(sequence)
    task = ' '.join(
        '..' if number == correct_answer else str(number) for number in sequence
    )

    return task, correct_answer

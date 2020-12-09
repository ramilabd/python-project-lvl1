# -*- coding:utf-8 -*-

"""Functions of the game "Brain-progression."""

from random import choice

GAME_RULE = 'What number is missing in the progression?'


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


def get_arithmetic_progression(start=3, step=5, len_sequence=10):
    """
    Get an increasing arithmetic progression.

    Parameters:
        start: int (by default 3)
        step: int (by default 5)
        len_sequence: int (by default 10)

    Returns:
        list
    """
    sequence = []

    while len_sequence:
        sequence.append(start)
        start += step
        len_sequence -= 1

    return sequence

# -*- coding:utf-8 -*-

"""Functions of the game "Brain-progression."""

from random import choice, randint

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


def get_arithmetic_progression():
    """
    Get an increasing arithmetic progression.

    Parameters are missing.

    Returns:
        list
    """
    start = randint(1, 10)
    step = randint(1, 10)
    len_sequence = 10
    sequence = []

    while len_sequence:
        sequence.append(start)
        start += step
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

# -*- coding:utf-8 -*-

"""Game engine."""

import prompt

ROUNDS_COUNT = 3


def engine(game):
    """
    Game engine.

    Parameters:
        game: module of the game

    Returns: None
    """
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name_user))
    print(game.GAME_RULE)

    for _ in range(ROUNDS_COUNT):
        task, correct_answer = game.get_task_and_solution()
        print('Question: {0}'.format(task))
        answer_user = prompt.string('Your answer: ')
        if answer_user == correct_answer:
            print('Correct!')
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    else:
        print('Congratulations, {0}!'.format(name_user))


def show_game_over(answer_user, correct_answer, name_user):
    """
    Show that the user's answer is incorrect and offers to play again.

    Parameters:
        answer_user: str or int
        correct_answer: str or int
        name_user: str

    Returns: None
    """
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'".format(
        answer_user,
        correct_answer,
    ))
    print("Let's try again, {0}!".format(name_user))

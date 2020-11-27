# -*- coding:utf-8 -*-

"""The module of user interaction."""

from sys import exit

import prompt


def greeting(game_rules=None):
    """
    Show a greeting and rules of the game.

    Parameters:
        game_rules: str (by default == None)

    Returns: None
    """
    print('Welcome to the Brain Games!')
    if game_rules:
        print(game_rules)
        print()
    else:
        print()


def say_hello():
    """
    Greets the user.

    Parameters are missing.

    Returns:
        str
    """
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!\n\n'.format(name_user))
    return name_user


def show_task(task):
    """
    Show question.

    Parameters:
        task: str

    Returns: None
    """
    print('Question: {0}'.format(task))


def get_answer_user(game_module, tries=3):
    """
    Get the user's response.

    Parameters:
        game_module: module of the game
        tries: int (by default == 3)

    Returns:
        str or int
    """
    if tries == 0:
        exit('Attempts ended. Start the game again.')

    answer_user = prompt.string('Your answer: ')
    verified_answer = game_module.is_correct_data(answer_user)

    if verified_answer[0]:
        return verified_answer[1]
    else:
        report_incorrect_data(verified_answer[1])

    return get_answer_user(game_module, tries - 1)


def report_incorrect_data(verified_answer):
    """
    Inform about incorrect data entry.

    Parameters:
        verified_answer: str

    Returns: None
    """
    print(verified_answer)


def confirm_correct_answer(name_user=''):
    """
    Show that the user won.

    Parameters:
        name_user: str (by default == '')

    Returns: None
    """
    if name_user:
        print('Congratulations, {0}!'.format(name_user))
    else:
        print('Correct')


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

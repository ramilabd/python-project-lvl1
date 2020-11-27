# -*- coding:utf-8 -*-

"""Welcome user."""

import prompt


def welcome_user():
    """
    Welcome to the game.

    Parameters are missing.

    Returns: None
    """
    print('Welcome to the Brain Games!')
    name_user = prompt.string('May I have your name? ')
    print('Hello, {0}!\n\n'.format(name_user))

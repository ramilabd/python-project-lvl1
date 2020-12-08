# -*- coding:utf-8 -*-

"""Game engine."""

from sys import exit

import prompt

from brain_games.cli import welcome_user

ROUND = 3


def game_loop(game_module):
    """
    Game engine.

    Parameters:
        game_module: module of the game

    Returns: None
    """
    name_user = welcome_user()
    print(game_module.GAME_RULE)

    counter = 0
    while counter < ROUND:
        task, correct_answer = game_module.get_task_and_solution()
        print('Question: {0}'.format(task))
        answer_user = get_correct_answer_user(game_module)
        if answer_user == correct_answer:
            print('Correct!')
            counter += 1
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    else:
        print('Congratulations, {0}!'.format(name_user))


def get_correct_answer_user(game_module, tries=3):
    """
    Get the correct user respons.

    Parameters:
        game_module: module of the game
        tries: int

    Returns:
        str or int
    """
    if tries == 0:
        exit('Attempts ended. Start the game again.')

    answer_user = prompt.string('Your answer: ')
    game_name = game_module.__name__.rsplit('.')[-1]

    if game_name in {'calc', 'gcd', 'progression'}:
        try:
            return int(answer_user)
        except ValueError:
            print('{0} - invalid data, enter an integer.'.format(
                answer_user,
            ))
            get_correct_answer_user(game_module, tries - 1)

    if game_name in {'even', 'prime'} and answer_user in {'yes', 'no'}:
        return answer_user
    else:
        print('{0} - invalid data, enter an "yes" or "no".'.format(
            answer_user,
        ))
        get_correct_answer_user(game_module, tries - 1)


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

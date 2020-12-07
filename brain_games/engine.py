# -*- coding:utf-8 -*-

"""Game engine."""

from brain_games.cli import welcome_user
from brain_games.view import (
    confirm_correct_answer,
    get_correct_answer_user,
    show_game_over,
    show_rules_game,
    show_task,
)

ROUNDS_COUNT = 3


def game_engine(game_module):
    """
    Game engine.

    Parameters:
        game_module: module of the game

    Returns: None
    """
    name_user = welcome_user()
    show_rules_game(game_module)

    counter = 0
    while counter < ROUNDS_COUNT:
        task, correct_answer = game_module.get_task_and_solution()
        show_task(task)
        answer_user = get_correct_answer_user(game_module)
        if answer_user == correct_answer:
            confirm_correct_answer()
            counter += 1
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    else:
        confirm_correct_answer(name_user)

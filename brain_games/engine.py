# -*- coding:utf-8 -*-

"""Game engine."""

from brain_games.view import (
    confirm_correct_answer,
    get_answer_user,
    greeting,
    say_hello,
    show_game_over,
    show_task,
)

ROUNDS = 3


def game_loop(game_module):
    """
    Game engine.

    Parameters:
        game_module: module of the game

    Returns: None
    """
    greeting(game_module.GAME_RULE)
    name_user = say_hello()

    counter = 0
    while counter < ROUNDS:
        task, correct_answer = game_module.generator_task_and_solution()
        show_task(task)
        answer_user = get_answer_user(game_module)
        if answer_user == correct_answer:
            confirm_correct_answer()
            counter += 1
            continue
        show_game_over(answer_user, correct_answer, name_user)
        break
    if counter == 3:
        confirm_correct_answer(name_user)

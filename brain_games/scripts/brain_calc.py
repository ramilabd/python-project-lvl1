# -*- coding:utf-8 -*-

"""The script start the game 'Brain-calc."""

from brain_games.engine import game_loop
from brain_games.games import calc


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    game_loop(calc)


if __name__ == '__main__':
    main()

# -*- coding:utf-8 -*-

"""The script start the game 'Brain-even."""

from brain_games.engine import game_engine
from brain_games.games import even


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    game_engine(even)


if __name__ == '__main__':
    main()

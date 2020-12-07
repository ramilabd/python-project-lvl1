# -*- coding:utf-8 -*-

"""The script start the game 'Brain-progression."""

from brain_games.engine import game_engine
from brain_games.games import progression


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    game_engine(progression)


if __name__ == '__main__':
    main()

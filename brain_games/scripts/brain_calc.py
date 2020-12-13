# -*- coding:utf-8 -*-

"""The script start the game 'Brain-calc."""

from brain_games.engine import engine
from brain_games.games import calc


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    engine(calc)


if __name__ == '__main__':
    main()

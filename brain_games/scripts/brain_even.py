# -*- coding:utf-8 -*-

"""The script start the game 'Brain-even."""

from brain_games.engine import engine
from brain_games.games import even


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    engine(even)


if __name__ == '__main__':
    main()

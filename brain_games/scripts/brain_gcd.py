# -*- coding:utf-8 -*-

"""The script start the game 'Brain-gcd."""

from brain_games.engine import engine
from brain_games.games import gcd


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    engine(gcd)


if __name__ == '__main__':
    main()

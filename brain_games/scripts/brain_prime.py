# -*- coding:utf-8 -*-

"""The script start the game 'Brain-prime."""

from brain_games.engine import engine
from brain_games.games import prime


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    engine(prime)


if __name__ == '__main__':
    main()

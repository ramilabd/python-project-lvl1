# -*- coding:utf-8 -*-

"""The script start the game 'Brain-prime."""

from brain_games.engine import game_loop
from brain_games.games import prime


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    game_loop(prime)


if __name__ == '__main__':
    main()

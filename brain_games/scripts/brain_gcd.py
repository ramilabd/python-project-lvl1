# -*- coding:utf-8 -*-

"""The script start the game 'Brain-gcd."""

from brain_games.engine import game_loop
from brain_games.games import gcd


def main():
    """
    Program start.

    Parameters are missing.

    Returns: None
    """
    game_loop(gcd)


if __name__ == '__main__':
    main()

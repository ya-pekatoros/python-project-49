#! /usr/bin/env python3
''' Initialization of the game brain-even from bash'''
import sys

from brain_games.cli import welcome_user

from brain_games.games import game_even


def main():
    ''' Initialization with greetings'''
    welcome_user()
    game_even()
    return sys.exit()


if __name__ == '__main__':
    main()

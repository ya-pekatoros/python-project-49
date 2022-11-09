#! /usr/bin/env python3
''' Initialization of the game brain-calc from bash'''
import sys

from brain_games.cli import welcome_user

from brain_games.games.calc import game_calc


def main():
    ''' Initialization with greetings'''
    welcome_user()
    game_calc()
    return sys.exit()


if __name__ == '__main__':
    main()

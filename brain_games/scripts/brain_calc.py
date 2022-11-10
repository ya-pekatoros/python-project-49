#! /usr/bin/env python3
''' Initialization of the game brain-calc from bash'''
import sys
from brain_games.games_logic import run_game
from brain_games.games import calc


def main():
    ''' Initialization with greetings'''
    run_game(calc)
    return sys.exit()


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
''' Initialization of the game brain-even from bash'''
import sys
from brain_games.games_logic import run_game
from brain_games.games import even


def main():
    ''' Game call'''
    run_game(even)
    return sys.exit()


if __name__ == '__main__':
    main()

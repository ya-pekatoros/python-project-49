#! /usr/bin/env python3
''' Initialization of the game brain-progression from bash'''
import sys
from brain_games.games_logic import run_game
from brain_games.games import progression


def main():
    ''' Game call'''
    run_game(progression)
    return sys.exit()


if __name__ == '__main__':
    main()

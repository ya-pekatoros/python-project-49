#! /usr/bin/env python3
''' Initialization of the game brain-gcd from bash'''
import sys
from brain_games.games_logic import run_game
from brain_games.games import gcd


def main():
    ''' Game call'''
    run_game(gcd)
    return sys.exit()


if __name__ == '__main__':
    main()

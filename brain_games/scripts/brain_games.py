#! /usr/bin/env python3
''' Greeting by the games from bash'''
import sys
from brain_games.cli import welcome_user


def main():
    ''' Initialization of greetings'''
    welcome_user()
    return sys.exit()


if __name__ == '__main__':
    main()

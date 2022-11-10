#! /usr/bin/env python3
'''Game-gcd logic'''

import random

TASK = 'Find the greatest common divisor of given numbers.'
BOTTOM_LIMIT = 1
TOP_LIMIT = 100


def get_game():
    ''' Main game-function of game-gcd. Describes the essence of the game'''
    first_number = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
    second_number = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
    question = f'{first_number} {second_number}'

    def gcd(first, second):
        '''Find a gcd of first and second numbers. I know about existing of
        math.gcd, but want to try recursive function'''
        if first == second:
            return first
        elif first > second:
            return gcd(first - second, second)
        else:
            return gcd(first, second - first)

    correct_answer = gcd(first_number, second_number)
    return question, str(correct_answer)

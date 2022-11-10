#! /usr/bin/env python3
'''Game-even logic'''

import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
BOTTOM_LIMIT = 1
TOP_LIMIT = 100


def get_game():
    ''' Main game-function of game-even. Describes the essence of the game'''
    question = random.randrange(BOTTOM_LIMIT, TOP_LIMIT)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, str(correct_answer)

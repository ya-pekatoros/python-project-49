#! /usr/bin/env python3
'''Game-prime logic'''

import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOWER_LIMIT = 1
TOP_LIMIT = 100


def get_game():
    ''' Main game-function of game-prime. Describes the essence of the game'''
    question = random.randrange(LOWER_LIMIT, TOP_LIMIT)

    correct_answer = 'yes'

    if question == 1:
        correct_answer = 'no'
    else:
        for i in range(2, question):
            if question % i == 0:
                correct_answer = 'no'

    return question, str(correct_answer)

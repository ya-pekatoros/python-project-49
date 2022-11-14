'''Game-even logic'''

import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'
LOW_LIMIT = 1
TOP_LIMIT = 100


def is_even(number):
    '''Returns True if given number is even'''
    return number % 2 == 0


def get_game():
    ''' Main game-function of game-even. Describes the essence of the game'''
    question = random.randrange(LOW_LIMIT, TOP_LIMIT)
    if is_even(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, str(correct_answer)

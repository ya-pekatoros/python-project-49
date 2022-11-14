'''Game-prime logic'''

import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'
LOW_LIMIT = 1
TOP_LIMIT = 100


def is_prime(number):
    '''Returns True if given number is prime'''
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_game():
    ''' Main game-function of game-prime. Describes the essence of the game'''
    question = random.randrange(LOW_LIMIT, TOP_LIMIT)
    if is_prime(question):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, str(correct_answer)

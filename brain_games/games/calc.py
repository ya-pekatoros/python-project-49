#! /usr/bin/env python3
'''Game-calc logic'''

import operator
import random

TASK = 'What is the result of the expression?'
LOWER_LIMIT = 1
TOP_LIMIT = 100

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_game():
    ''' Main game-function of game-calc. Describes the essence of the game'''
    first_number = random.randrange(LOWER_LIMIT, TOP_LIMIT)
    second_number = random.randrange(LOWER_LIMIT, TOP_LIMIT)
    math_operation = random.choice(['+', '-', '*'])
    question = f'{first_number} {math_operation} {second_number}'
    correct_answer = operations[math_operation](first_number, second_number)
    return question, str(correct_answer)

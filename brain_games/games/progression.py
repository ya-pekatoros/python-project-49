#! /usr/bin/env python3
'''Game-progression logic'''

import random

TASK = 'What number is missing in the progression?'
LOW_STEP_LIMIT = -10
TOP_STEP_LIMIT = 10
LOW_START_LIMIT = -100
TOP_START_LIMIT = 100
LOW_LENGTH_LIMIT = 5
TOP_LENGTH_LIMIT = 9


def make_progression(start, step, length):
    '''Generates arithmetic progression'''
    progression = []
    for i in range(length):
        progression.append(start + step * i)
    return progression


def generate_question(progression, missing_index):
    progression[missing_index] = '..'
    return ' '.join(map(str, progression))


def get_game():
    ''' Main game-function of game-progression.
        Describes the essence of the game'''
    step_variants = list(range(LOW_STEP_LIMIT, TOP_STEP_LIMIT))
    if 0 in step_variants:
        step_variants.remove(0)
    step = random.choice(step_variants)
    start = random.randrange(LOW_START_LIMIT, TOP_START_LIMIT)
    length = random.randrange(LOW_LENGTH_LIMIT, TOP_LENGTH_LIMIT)
    progression = make_progression(start, step, length)
    correct_answer = random.choice(progression[1:])
    missing_index = progression.index(correct_answer)
    question = generate_question(progression, missing_index)
    return question, str(correct_answer)

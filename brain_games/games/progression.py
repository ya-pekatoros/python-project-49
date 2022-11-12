#! /usr/bin/env python3
'''Game-progression logic'''

import random

TASK = 'What number is missing in the progression?'
LOWER_STEP_LIMIT = -10
TOP_STEP_LIMIT = 10
LOWER_START_LIMIT = -100
TOP_START_LIMIT = 100
LOWER_LENGTH_LIMIT = 4
TOP_LENGTH_LIMIT = 9


def get_game():
    ''' Main game-function of game-progression.
        Describes the essence of the game'''
    step = random.choice(list(range(LOWER_STEP_LIMIT, 0))
                         + list(range(1, TOP_STEP_LIMIT)))
    start = random.randrange(LOWER_START_LIMIT, TOP_START_LIMIT)
    length = random.randrange(LOWER_LENGTH_LIMIT, TOP_LENGTH_LIMIT)
    progression = []

    for i in range(length):
        progression.append(start + step * i)

    correct_answer = random.choice(progression)
    missing_index = progression.index(correct_answer)
    question = (
        f"{' '.join(map(str, progression[:missing_index]))}"
        f" .. {' '.join(map(str, progression[missing_index + 1:]))}"
    )

    return question, str(correct_answer)

#! /usr/bin/env python3
'''Game-even logic'''

import random

from brain_games.common_games_logic import common_games_logic


def game_even():
    ''' Main game-function of game-even. Describes the essence of the game'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins_count = 0
    is_game_continuing = True
    while is_game_continuing:
        question = random.randrange(1, 100)

        if question % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        is_game_continuing = common_games_logic(question, correct_answer,
                                                wins_count)

        wins_count += 1

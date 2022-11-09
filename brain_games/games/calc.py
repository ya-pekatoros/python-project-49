#! /usr/bin/env python3
'''Game-calc logic'''

import random

from brain_games.common_games_logic import common_games_logic

def game_calc():
    ''' Main game-function of game-calc. Describes the essence of the game'''
    print('What is the result of the expression?')
    wins_count = 0
    is_game_continuing = True

    while is_game_continuing:
        first_number = random.randrange(1, 100)
        second_number = random.randrange(1, 100)
        math_operation = random.choice(['+', '-', '*'])
        question = f'{first_number} {math_operation} {second_number}'
 
        if math_operation == '+':
            correct_answer = str(first_number + second_number)
        elif math_operation == '-':
            correct_answer = str(first_number - second_number)
        else:
            correct_answer = str(first_number * second_number)

        is_game_continuing = common_games_logic(question, correct_answer, wins_count)
        wins_count += 1

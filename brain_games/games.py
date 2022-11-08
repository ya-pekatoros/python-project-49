#! /usr/bin/env python3
''' Main games logics module'''

import random

import brain_games.cli


def game_even():
    ''' Main game-function of game-even. Describes the logic of the game'''
    print('Answer "yes" if the number is even, otherwise answer "no".')
    wins_count = 0
    while True:
        given_number = random.randrange(1, 100)
        print(f'Question: {given_number}')
        user_answer = input()
        print(f'Your answer: {user_answer}')

        if given_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if user_answer == correct_answer:
            wins_count += 1
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            break

        if wins_count == 3:
            print(f'Congratulations, {brain_games.cli.name}!')
            break

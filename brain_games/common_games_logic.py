#! /usr/bin/env python3
''' Main games logics module'''

import brain_games.cli


def common_games_logic(question, correct_answer, wins_count):
    '''Describes common rules and principles of brain-games'''
    print(f'Question: {question}')
    user_answer = input()
    print(f'Your answer: {user_answer}')
    if user_answer == correct_answer:
        wins_count += 1
        print('Correct!')
    else:
        print(f'"{user_answer}" is wrong answer ;(. '
              f'Correct answer was "{correct_answer}".')
        return False

    if wins_count == 3:
        print(f'Congratulations, {brain_games.cli.name}!')
        return False

    return True
    
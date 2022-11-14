''' Main games logics module'''

import prompt

NUMBER_OF_ROUNDS = 3


def run_game(game_name):
    '''Common rules and principles of brain-games'''
    user_name = prompt.string('Welcome to the Brain Games!\n'
                              'May I have your name?\n')
    print(f'Hello, {user_name}!')
    print(game_name.TASK)
    wins_count = 0
    while wins_count < NUMBER_OF_ROUNDS:
        question, correct_answer = game_name.get_game()
        print(f'Question: {question}')
        user_answer = input()
        print(f'Your answer: {user_answer}')
        if user_answer == correct_answer:
            wins_count += 1
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".'
                  f'\nLet\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')

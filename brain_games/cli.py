'''Greetings'''

import sys

import prompt

def welcome_user():
    '''Greetings'''
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name?\n')
    print(f'Hello,{name}!')
    return sys.exit()

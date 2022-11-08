#! /usr/bin/env python3
'''Greetings'''
import prompt

name = ''


def welcome_user():
    '''Greetings'''
    global name
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name?\n')
    print(f'Hello, {name}!')

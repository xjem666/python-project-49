#!/usr/bin/env python3

from random import randrange
def main():
    print("Welcome to the Brain Games!")
    print('May I have your name? ', end='')
    name = input()
    print("Hello", name)

def task():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    number = randrange(100)
    print("Question:", number)
    answer_ = input() #Yes or No
    print("Your answer:", answer_)
    if answer_ = "Yes":
        number % 2 = 0
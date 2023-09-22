import random
from random import choice
import prompt

from brain_games.utils import get_random_number


def get_math_sign_and_result(first_number, second_number):
    math_sign = choice(['+', '-', '*'])
    match math_sign:
        case '+':
            return math_sign, first_number + second_number
        case '-':
            return math_sign, first_number - second_number
        case '*':
            return math_sign, first_number * second_number


def run_calc():
    for _ in range(3):
        print("What is the result of the expression?")
        first_number, second_number = get_random_number(), get_random_number()
        math_sign, result = get_math_sign_and_result(first_number, second_number)
        print(f'Question {first_number} {math_sign} {second_number}')
        user_answer = prompt.string(f'Your answer:')
        if user_answer == str(result):
            print("Correct")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'. \n Let's try again!")
            return


run_calc()

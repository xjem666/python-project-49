#!/usr/bin/env python3
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
        correct_answer = get_math_sign_and_result(first_number, second_number)
        if user_answer == correct_answer:
            print("Correct")
        else:
            print('No')
            return


run_calc()
"""
1.Сделать калькулятор для проверки
2.Сделатьть игру для пользователя проверки калькулятора используя оператор if по типу  - >
 > > > > если первое число меньше второго то знак +
 > > > > если первое число больше знак -
 > > > > если первое число больше или равно знак умножить

3.Проверить что бы ответы совпадали
4.Сообщить верно или нет
"""

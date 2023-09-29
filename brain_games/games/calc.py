import random
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def get_math_sign_and_result(num1, num2):
    math_list = [
        ('+', num1 + num2),
        ('-', num1 - num2),
        ('*', num1 * num2)
    ]
    math_sign, result = random.choice(math_list)
    return math_sign, result


def brain_calc():
    num1, num2 = get_random_number(), get_random_number()
    math_sign, result = get_math_sign_and_result(num1, num2)
    question = f"{num1} {math_sign} {num2}"
    return question, str(result)


def run_calc_game():
    run_game(brain_calc, 'What is the result of the expression?')

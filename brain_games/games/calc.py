import random
from brain_games.engine import run_game
from brain_games.utils import get_random_number
from brain_games.const import CALC_INSTRUCTION, MATH_OPERATORS


def get_math_expression_and_result():
    num1, num2 = get_random_number(), get_random_number()
    math_operators = random.choice(MATH_OPERATORS)
    expression = f"{num1} {math_operators} {num2}"
    result = eval(expression)
    return ..., str(result)


def run_calc_game():
    run_game(get_math_expression_and_result, CALC_INSTRUCTION)

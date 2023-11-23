import random
from brain_games.engine import run_game
from brain_games.utils import get_random_number
from brain_games.const import CALC_INSTRUCTION, MATH_OPERATORS


def get_math_question_and_result():
    num1, num2 = get_random_number(), get_random_number()
    math_sign = random.choice(MATH_OPERATORS)
    question = f"{num1} {math_sign} {num2}"
    return question, str(eval(question))


def run_calc_game():
    run_game(get_math_question_and_result, CALC_INSTRUCTION)

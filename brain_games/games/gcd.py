#!/usr/bin/env python3
import math
from brain_games.utils import get_random_number
from brain_games.engine import run_game
from brain_games.const import NOD_INSTRUCTION


def get_nod(num1, num2):
    return math.gcd(num1, num2)


def get_problem_num_and_question():
    num1, num2 = get_random_number(), get_random_number()
    question = f'{num1} {num2}'
    result = str(get_nod(num1, num2))
    return question, result


def run_gcd_game():
    run_game(get_problem_num_and_question, NOD_INSTRUCTION)

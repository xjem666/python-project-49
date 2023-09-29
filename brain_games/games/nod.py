#!/usr/bin/env python3
import math
from brain_games.utils import get_random_number
from brain_games.engine import run_game


def get_nod(num1, num2):
    return math.gcd(num1, num2)


def brain_nod():
    num1, num2 = get_random_number(), get_random_number()
    question = f'{num1} {num2}'
    result = str(get_nod(num1, num2))
    return question, result


def run_nod():
    run_game(brain_nod, 'Find the greatest common divisor of given numbers.')

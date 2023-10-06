from brain_games.engine import run_game
from brain_games.utils import get_random_number
from brain_games.const import PRIME_INSTRUCTION


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def brain_prime():
    problem_num = get_random_number()
    answer = 'yes' if is_prime(problem_num) else 'no'
    return problem_num, answer


def run_brain_prime():
    run_game(brain_prime, PRIME_INSTRUCTION)

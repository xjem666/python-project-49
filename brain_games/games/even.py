from brain_games.engine import run_game
from brain_games.utils import get_random_number


def is_even(num):
    return num % 2 == 0


def brain_even():
    problem_num = get_random_number()
    answer = 'yes' if is_even(problem_num) else 'no'
    return problem_num, answer


def run_brain_even():
    run_game(brain_even, 'Answer "yes" if the number is even, '
                         'otherwise answer "no".')

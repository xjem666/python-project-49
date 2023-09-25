import math
import prompt
from brain_games.utils import get_random_number


def run_nod():
    for _ in range(3):
        first_number, second_number = get_random_number(), get_random_number()
        correct_answer = math.gcd(first_number, second_number)
        print(f"Question {first_number}, {second_number}")
        user_answer = prompt.string(f'Your answer - >')
        if user_answer == str(correct_answer):
            print("Correct")
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was - > {correct_answer}')
            return


run_nod()

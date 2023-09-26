import random

import prompt


def is_even(num):
    return num % 2 == 0


def run_even_game():
    print('Answer "Yes" if the number is even, otherwise answer "No".')
    for _ in range(3):
        random_num = random.randint(1, 11)
        print(f'Question: {random_num}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = "Yes" if is_even(random_num) else "No"
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}")
            return

run_even_game()

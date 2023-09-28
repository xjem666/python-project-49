import prompt
from brain_games.utils import get_random_number

# Const.py
AMOUNT_OF_ROUNDS = 3
EVEN_INSTUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_promblem_num_and_result():
    promblem_num = get_random_number()
    result = 'yes' if is_even(promblem_num) else 'no'
    return promblem_num, result


def run_game(instuction: str, get_question_and_answer: callable):
    user_name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {user_name}!\n{instuction}')
    for _ in range(AMOUNT_OF_ROUNDS):
        question, answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.Correct answer was'{answer}'\nLet's try again, {user_name}! ")
            return
    print(f'Congratulations, {user_name}!')


run_game(EVEN_INSTUCTION, get_promblem_num_and_result)

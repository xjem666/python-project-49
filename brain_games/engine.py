import prompt
from brain_games.const import AMOUNT_OF_ROUNDS


def run_game(get_question_and_answer, instruction):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}\n{instruction}')
    for _ in range(AMOUNT_OF_ROUNDS):
        question, result = get_question_and_answer()
        user_input = prompt.string(f'Question: {question}\nYour answer: ')
        if result == user_input:
            print('Correct!')
        else:
            print(
                f"'{user_input}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!")  # noqa
            return
    print(f"Congratulations, {name}!")

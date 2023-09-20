import random

import prompt

def main():
    print("Welcome to the brain games!")
    print('May i have your name? ', end='')
    name = input()
    print("Hello", name)


main()

def is_even(num):
    return num % 2 == 0


def is_even_str(num):
    return "yes" if num % 2 == 0 else "no"



def game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_num = random.randint(1, 11)
        print(f'Question {random_num}')
        user_answer = prompt.string('Your answer:')
        correct_answer = "Yes" if is_even(random_num) else "No"
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"{correct_answer} is wrong answer ;(. Correct answer was {user_answer}")



game()
print("Congratulations")


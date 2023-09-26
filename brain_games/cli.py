import prompt


def welcome_user():
    name = prompt.string("Welcome to the Brain Games! \n May I Have your name? ")
    print(f"Hello, {name}")

import prompt


def welcome_user():
    name = prompt.string("Welcome to the brain games! \n May i Have your name? ")
    print(f"Hello, {name}")

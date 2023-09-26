import prompt
from brain_games.utils import get_random_number


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def run_prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        number = get_random_number()

        user_answer = prompt.string(f"Question: {number} - > ")

        if is_prime(number) and user_answer == "yes":
            print("Correct!")
        elif not is_prime(number) and user_answer == "no":
            print("Correct!")
        else:
            print(f"{number} is wrong answer ;(. {number} is prime." if is_prime(number) else f"{number} not prime.")
            return


run_prime_game()

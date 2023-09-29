import random


# Создание прогресси
def generate_progression(length):
    start = random.randint(1, 10)
    diff = random.randint(1, 10)
    end = start + (length - 1) * diff
    progression = list(range(start, end + 1, diff))
    return progression


# Прячу число
def hide_element(progression):
    hidden_index = random.randint(0, len(progression) - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = ".."
    return progression, hidden_value


# Игра
def run_progression_game():
    print("What number is missing in the progression?")
    for _ in range(3):
        length = 10
        progression = generate_progression(length)
        progression_with_hidden, hidden_value = hide_element(progression)
        print(" ".join(str(num) for num in progression_with_hidden))

        guess = int(input("Your answer: "))

        if guess == hidden_value:
            print("Correct!")
        else:
            print(f"{guess} is wrong answer ;(. Correct answer was {hidden_value}")

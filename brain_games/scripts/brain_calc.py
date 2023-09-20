import random
from random import choice
import prompt

f_number = random.randint(0, 100)
s_number = random.randint(0, 80)
operation = ['+', '-', '*']





def main():
    print("Welcome to the brain games!")
    print('May i have your name? ', end='')
    name = input()
    print("Hello", name)


def user_cult():
    print(f'What the result of the expression?')
    for _ in range(3):
        print(f"Question {f_number} {choice(operation)} {s_number}")
        user_answer = prompt.string('Your Answer - >')


main()
user_cult()

"""
1.Сделать калькулятор для проверки
2.Сделатьть игру для пользователя проверки калькулятора используя оператор if по типу  - >
 > > > > если первое число меньше второго то знак +
 > > > > если первое число больше знак -
 > > > > если первое число больше или равно знак умножить

3.Проверить что бы ответы совпадали
4.Сообщить верно или нет
"""

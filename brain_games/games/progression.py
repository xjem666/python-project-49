from random import randint

from brain_games.const import PROGRESSION_LENGTH, PROGRESSION_INSTRUCTION
from brain_games.engine import run_game
from brain_games.utils import get_random_number


def create_progression(first_num, diff, missed_num_ind, progression_length):
    return ' '.join(['..' if i == missed_num_ind else str(first_num + i * diff)
                     for i in range(progression_length)])


def get_progression_and_missed_num():
    first_num, diff = get_random_number(), get_random_number()
    missed_num_ind: int = randint(0, PROGRESSION_LENGTH - 1)
    question = create_progression(
        first_num, diff, missed_num_ind, PROGRESSION_LENGTH
    )
    result = str(first_num + missed_num_ind * diff)
    return question, result


def run_progression():
    run_game(get_progression_and_missed_num, PROGRESSION_INSTRUCTION)

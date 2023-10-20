from random import randint

from brain_games.const import PROGRESSION_LENGTH
from brain_games.engine import run_game
from brain_games.utils import get_random_number
from brain_games.const import PROGRESSION_INSTRUCTION


def brain_progression():
    first_num, diff = get_random_number(), get_random_number()
    missed_num_ind = randint(0, PROGRESSION_LENGTH - 1)
    pg = ' '.join(['..' if i == missed_num_ind else str(first_num + i * diff)
                   for i in range(PROGRESSION_LENGTH)
                   ])
    result = str(first_num + missed_num_ind * diff)
    return pg, result


def run_brain_progression():
    run_game(brain_progression, PROGRESSION_INSTRUCTION)

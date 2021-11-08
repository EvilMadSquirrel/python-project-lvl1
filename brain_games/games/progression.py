"""Logic module for brain-progression game."""
import random

DESCRIPTION = 'What number is missing in the progression?'

MAX_START = 20
MIN_LEN = 5
MAX_LEN = 10
MIN_DIFF = 2
MAX_DIFF = 10


def _generate_progression():
    """Do generate 'random' progression.

    Returns:
        list(int): Progression
    """
    prog_len = random.randint(MIN_LEN, MAX_LEN)
    diff = random.randint(MIN_DIFF, MAX_DIFF)
    start = random.randint(0, MAX_START)
    return [start + diff * idx for idx in range(prog_len)]


def generate_round():
    prog = _generate_progression()
    missing_position = random.randint(0, len(prog) - 1)
    missing_element = prog[missing_position]
    prog[missing_position] = '..'
    prog = list(map(str, prog))
    string_question = ' '.join(prog)
    return string_question, missing_element

"""Logic module for brain-progression game."""
import random

DESCRIPTION = 'What number is missing in the progression?'

_MAX_START = 20
_MIN_LEN = 5
_MAX_LEN = 10
_MIN_DIFF = 2
_MAX_DIFF = 10


def _generate_progression(prog_len, diff, start):
    """Do generate 'random' progression.

    Args:
        prog_len: Length of progression
        diff: Difference between elements
        start: Start number of progression

    Returns:
        Progression

    """
    return [start + diff * idx for idx in range(prog_len)]


def generate_round():
    """Do generate question and answer.

    Returns:
        tuple(str, int): String question for print and answer
    """
    prog_len = random.randint(_MIN_LEN, _MAX_LEN)
    diff = random.randint(_MIN_DIFF, _MAX_DIFF)
    start = random.randint(0, _MAX_START)
    prog = _generate_progression(prog_len, diff, start)
    missing_position = random.randint(0, len(prog) - 1)
    missing_element = prog[missing_position]
    prog[missing_position] = '..'
    prog = list(map(str, prog))
    string_question = ' '.join(prog)
    return string_question, missing_element

"""Logic module for brain-progression game."""
import random

DESCRIPTION = 'What number is missing in the progression?'

MAX_START = 20
MIN_LEN = 5
MAX_LEN = 10
MIN_DIFF = 2
MAX_DIFF = 10


def make_progression():
    """Do generate 'random' progression.

    Returns:
        list(str): Progression
    """
    prog_len = random.randint(MIN_LEN, MAX_LEN)
    diff = random.randint(MIN_DIFF, MAX_DIFF)
    start = random.randint(0, MAX_START)
    return [str(start + diff * idx) for idx in range(prog_len)]


def generate_question():
    """Do generate question with progression.

    Returns:
        str: Right answer
    """
    prog = make_progression()
    missing_position = random.randint(0, len(prog) - 1)
    missing_element = prog[missing_position]
    prog[missing_position] = '..'

    print('Question: {0}'.format(' '.join(prog)))
    return int(missing_element)


def check_answer(right_answer, answer):
    """Do check player answer.

    Args:
        right_answer (int): Right answer
        answer (str): Player answer

    Returns:
        bool: Correct or incorrect player answer.
    """
    player_answer = 0
    try:
        player_answer = int(answer)
    except ValueError:
        print('Incorrect answer')
        return False
    if player_answer == right_answer:
        print('Correct')
        return True
    print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
    print("Correct answer was '{0}'.".format(right_answer))
    return False

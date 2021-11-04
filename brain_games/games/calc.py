"""Logic module for brain-calc game."""
import random

DESCRIPTION = 'What is the result of the expression?'


def generate_expression():
    """Do generate question.

    Returns:
        tuple:
            [0], [1]: numbers for calculation
            [2]: calculation operator +, -, or *
    """
    operators = ('+', '-', '*')
    limit = 50
    question = (
        random.randint(0, limit),
        random.randint(0, limit),
        random.choice(operators),
    )
    q_string = 'Question: {0} {2} {1}'.format(*question)
    print(q_string)
    return question


def check_expression(question, answer):
    """Do check player answer.

    Args:
        question (tuple): Two numbers and operator
        answer (str): Player answer

    Returns:
        bool: Correct or incorrect player answer.
    """
    num1, num2, operator = question
    right_answers = {
        '+': num1 + num2,
        '*': num1 * num2,
        '-': num1 - num2,
    }
    player_answer = 0
    try:
        player_answer = int(answer)
    except ValueError:
        print('Incorrect answer')
        return False
    if player_answer == right_answers[operator]:
        print('Correct')
        return True
    print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
    print("Correct answer was '{0}'.".format(right_answers[operator]))
    return False

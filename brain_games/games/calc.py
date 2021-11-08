"""Logic module for brain-calc game."""
import random

DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ('+', '-', '*')
LIMIT = 50


def _generate_answer(question):
    num1, operator, num2 = question
    right_answers = {
        '+': num1 + num2,
        '*': num1 * num2,
        '-': num1 - num2,
    }
    return right_answers[operator]


def generate_round():
    question = (
        random.randint(0, LIMIT),
        random.choice(OPERATORS),
        random.randint(0, LIMIT),
    )
    answer = _generate_answer(question)
    string_question = '{0} {1} {2}'.format(*question)

    return string_question, answer

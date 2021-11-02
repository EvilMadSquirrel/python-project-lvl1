#!/usr/bin/env python
"""Even game script."""
import random

import prompt
from brain_games.game_utils import finish_game, welcome_user


def check_answer(num, answer):
    """Do check player answer.

    Args:
        num (int): Number to check - even or not.
        answer (string): Player answer 'yes', 'no' or something else.

    Returns:
        bool: Correct or incorrect player answer.
    """
    correct_even = answer == 'yes' and num % 2 == 0
    correct_odd = answer == 'no' and num % 2 != 0
    if answer not in ('yes', 'no'):
        print('Incompatible answer')
        return False
    elif correct_even or correct_odd:
        print('Correct!')
        return True
    right_answer = 'yes' if answer == 'no' else 'no'
    print("'{0}' is wrong answer ;(. ".format(answer), end='')
    print("Correct answer was '{0}'.".format(right_answer))
    return False


def play_game():
    """Plays the game.

    Returns:
        string: 'win' if player wins,
                'loss' if player not wins or unexpected answer
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        num = random.randint(0, 1000)
        print('Question: {0}'.format(num))
        player_answer = prompt.string('Your answer: ')
        if check_answer(num, player_answer):
            correct_answers += 1
        else:
            return 'loss'
    return 'win'


def main():
    """Do launch and controls even game."""
    player_name = welcome_user()
    game_result = play_game()
    finish_game(player_name, game_result)


if __name__ == '__main__':
    main()

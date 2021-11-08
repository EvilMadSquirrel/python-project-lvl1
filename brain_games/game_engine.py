"""Game engine."""

from brain_games import cli

MAX_ROUNDS = 3
RIGHT_TEXT_ANSWERS = {'yes', 'no'}


def _normalize_answer(right_answer, player_answer):
    if type(right_answer) is int:
        try:
            player_answer = int(player_answer)
        except ValueError:
            print('Incorrect answer')
            return
    if type(right_answer) is str and player_answer not in RIGHT_TEXT_ANSWERS:
        print('Incorrect answer')
        return
    return player_answer


def play_game(game):
    player_name = cli.welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    while correct_answers < MAX_ROUNDS:
        question, right_answer = game.generate_round()
        player_answer = cli.ask_question(question)
        player_answer = _normalize_answer(right_answer, player_answer)
        if not player_answer:
            print("Let's try again, {0}!".format(player_name))
            return
        elif player_answer == right_answer:
            print('Correct')
            correct_answers += 1
        else:
            print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
            print("Correct answer was '{0}'.".format(right_answer))
            print("Let's try again, {0}!".format(player_name))
            return
    print('Congratulations, {0}!'.format(player_name))

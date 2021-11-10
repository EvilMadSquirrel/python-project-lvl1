"""Game engine."""

from brain_games import cli

_MAX_ROUNDS = 3


def play_game(game):
    """Do control all games.

    Args:
        game: Game module

    """
    player_name = cli.welcome_user()
    print(game.DESCRIPTION)
    for _ in range(_MAX_ROUNDS):
        question, right_answer = game.generate_round()
        player_answer = cli.ask_question(question)
        if player_answer == str(right_answer):
            print('Correct')
        else:
            print("'{0}' is wrong answer ;(. ".format(player_answer), end='')
            print("Correct answer was '{0}'.".format(right_answer))
            print("Let's try again, {0}!".format(player_name))
            break
    else:
        print('Congratulations, {0}!'.format(player_name))

"""Game engine."""

from brain_games import cli

_MAX_ROUNDS = 3
_RIGHT_TEXT_ANSWERS = ('yes', 'no')


def _normalize_answer(right_answer, answer):
    """Do check player answer is correct.

    Args:
        right_answer: Correct answer
        answer: Player answer

    Returns:
        Player answer of correct type
    """
    if isinstance(right_answer, int):
        try:
            answer = int(answer)
        except ValueError:
            print('Incorrect answer')
            return None
    if isinstance(right_answer, str) and answer not in _RIGHT_TEXT_ANSWERS:
        print('Incorrect answer')
        return None
    return answer


def play_game(game):
    """Do control all games.

    Args:
        game: Game module

    """
    player_name = cli.welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    while correct_answers < _MAX_ROUNDS:
        question, right_answer = game.generate_round()
        player_answer = cli.ask_question(question)
        player_answer = _normalize_answer(right_answer, player_answer)
        if player_answer is None:
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
    if correct_answers == _MAX_ROUNDS:
        print('Congratulations, {0}!'.format(player_name))

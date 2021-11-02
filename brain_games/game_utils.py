"""Functions for all games."""
import prompt


def welcome_user():
    """Welcomes user and asks name.

    Returns:
        string: Player name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    return name


def finish_game(name, game_result):
    """Do shows result of game.

    Args:
        name (string): Player name
        game_result (string): Result of the game ('win' or 'loss')
    """
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    else:
        print("Let's try again, {0}!".format(name))

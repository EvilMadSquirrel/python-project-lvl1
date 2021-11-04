"""Game engine."""
import prompt


def welcome_user() -> str:
    """Welcomes user and asks name.

    Returns:
        str: Player name
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    return name


def _ask_questions(gen_func, check_func) -> str:
    """Do ask questions.

    Args:
        gen_func (function): Function that generates question
        check_func (function): Function that checks answer

    Returns:
        str: 'win' if player wins,
            'loss' if player not wins or unexpected answer
    """
    correct_answers = 0
    while correct_answers < 3:
        question = gen_func()
        player_answer = prompt.string('Your answer: ')
        if check_func(question, player_answer):
            correct_answers += 1
        else:
            return 'loss'
    return 'win'


def _finish_game(name: str, game_result: str):
    """Do show result of game.

    Args:
        name (str): Player name
        game_result (str): Result of the game ('win' or 'loss')
    """
    if game_result == 'win':
        print('Congratulations, {0}!'.format(name))
    else:
        print("Let's try again, {0}!".format(name))


def play_game(desc: str, gen_func, check_func):
    """Do control all games.

    Args:
        desc (str): Game description
        gen_func (function): Function that generates question
        check_func (function): Function that checks answer
    """
    player_name = welcome_user()
    print(desc)
    game_result = _ask_questions(gen_func, check_func)
    _finish_game(player_name, game_result)

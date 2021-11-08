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


def ask_question(question):
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')
    return answer

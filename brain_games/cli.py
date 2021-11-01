"""Command line interface for brain-games."""
import prompt


def welcome_user():
    """Ask user name and welcome user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {n}!'.format(n=name))

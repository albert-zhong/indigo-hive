from random import choice
from string import ascii_lowercase, digits


def random_string(size=10, chars=ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size))

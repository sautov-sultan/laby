from random import choice
from string import ascii_letters as al, digits as d


def gen_psw(length: int) -> str:
    return ''.join([choice(al + d) for _ in range(length)])


print(gen_psw(10))
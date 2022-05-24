"""
kata link: https://www.codewars.com/kata/592e830e043b99888600002d
kata kyu: 7
"""


def encode(message, key):
    str_key = str(key)
    return [ord(let) - 96 + int(str_key[i % len(str_key)]) for i, let in enumerate(message)]

"""
kata link: https://www.codewars.com/kata/57eba158e8ca2c8aba0002a0
kata kyu: 7
"""


def last(s):
    return sorted(s.split(), key=lambda ch: ch[-1])

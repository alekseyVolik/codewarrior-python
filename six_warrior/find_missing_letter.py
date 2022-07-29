"""
kata link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2
kata kyu: 6
"""


def find_missing_letter(chars):
    for l1, l2 in zip(chars, [chr(n) for n in range(ord(chars[0]), ord(chars[-1]))]):
        if l1 != l2:
            return l2

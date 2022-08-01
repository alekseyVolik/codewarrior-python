"""
kata link: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
kata kyu: 6
"""

from collections import Counter


def duplicate_encode(word: str) -> str:
    letter_counter = Counter(word.lower())
    return ''.join((')' if letter_counter[word] > 1 else '(' for word in word.lower()))

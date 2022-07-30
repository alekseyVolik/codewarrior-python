"""
kata link: https://www.codewars.com/kata/5264d2b162488dc400000001
kata kyu: 6
"""


def spin_words(sentence: str) -> str:
    return ' '.join((word if len(word) < 5 else word[::-1] for word in sentence.split()))

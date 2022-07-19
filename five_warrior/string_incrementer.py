"""
kata link: https://www.codewars.com/kata/54a91a4883a7de5d7800009c
kata kyu: 5
"""

from re import findall


def increment_string(strng):
    matches = findall(r'\d+', strng)
    if matches:
        digits = matches[-1]
        return f"{strng[:-(len(digits))]}{int(digits) + 1:0>{len(digits)}}"
    else:
        return f"{strng}1"

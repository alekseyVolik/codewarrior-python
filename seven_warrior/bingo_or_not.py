"""
kata link: https://www.codewars.com/kata/5a1ee4dfffe75f0fcb000145
kata kyu: 7
"""


def bingo(array):
    unique_nums = set(array)
    bingo_nums = set((ord(ch) - 96 for ch in 'bingo'))
    return 'WIN' if bingo_nums.issubset(unique_nums) else 'LOSE'

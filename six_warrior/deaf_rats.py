"""
kata link: https://www.codewars.com/kata/598106cb34e205e074000031
kata kyu: 6
"""


def count_deaf_rats(town):
    rat_direction = {'left': 'O~', 'right': '~O'}
    true_dir = 'right'
    deaf_rate = 0
    previous_ch = ''
    for ch in town:
        if ch == 'P':
            true_dir = 'left'
        if (previous_ch == '~' and ch == 'O') or (previous_ch == 'O' and ch == '~'):
            if rat_direction[true_dir] != (previous_ch + ch):
                deaf_rate += 1
            previous_ch = ''
        else:
            previous_ch = ch
    return deaf_rate

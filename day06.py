"""
day06, simple but a little strange.
Part B, YUK. Going to have to be a lot more careful in my whole parsing.
"""

import pytest
from helpers import load_tokens, load_lines


def day06a(fname):
    data = load_tokens(fname)
    # big 2d array
    total = 0
    wid, hig = len(data[0]), len(data)
    for x in range(wid):
        if data[-1][x] == "+":
            t = 0
            for y in range(hig - 1):
                t += int(data[y][x])
            total += t
        else:
            t = 1
            for y in range(hig - 1):
                t *= int(data[y][x])
            total += t
    return total


def find_number(data, x):
    "gets the number in the column X"
    hig = len(data)
    result = ""
    for y in range(hig - 1):
        result += data[y][x]
    return result.strip()


def day06b(fname):
    data = load_lines(fname)
    wid = len(data[0])
    # looking at the data, it clear we can use the position of the symbol of the last level to determine the MSB.
    # relying on that
    total = 0
    symbol, acc = "", 0
    for x in range(wid):
        if symbol == "":
            symbol = data[-1][x]
            acc = int(find_number(data, x))
        else:
            num = find_number(data, x)
            if num == "":
                # its empty: add accumulator to the total & clear it
                total += acc
                symbol, acc = "", 0
            else:
                if symbol == "+":
                    acc += int(num)
                else:
                    acc *= int(num)
    # edge case: add final acc
    total += acc

    return total


################################################################
if __name__ == "__main__":
    print("day06a", day06a("input06.txt"))
    print("day06b", day06b("input06.txt"))

################################################################


def test_day06a():
    assert day06a("test06.txt") == 4277556


def test_day06b():
    assert day06b("test06.txt") == 3263827

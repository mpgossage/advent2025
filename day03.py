"""
day03 part A: simple way to work
part B: oh help, a simple brute force of 12 digits is not going to be quick (esp looking at the real input)
So proper algol is going to be needed. This will also be a generic routine which could do part A 
"""

import pytest
from helpers import load_int_grid


def high_joltage(line):
    "highest joltage possible"
    # simple brute force for now
    high = 0
    ln = len(line)
    for i in range(ln):
        for j in range(i + 1, ln):
            val = 10 * line[i] + line[j]
            high = max(val, high)
    return high


def highest_digit(line, st, ed):
    idx, mx = st, line[st]
    for i in range(st + 1, ed + 1):
        if line[i] > mx:
            idx, mx = i, line[i]
    return idx, mx


def high_joltage2(line, digits):
    """
    Algol as follows:
    assume(specific): we want the largest 2 digit number from a list of 10 digits
    index i0 is largest digit in the range (0..8) inclusive
    index i1 is largest digit in the range (i0+1..9) inclusive

    assume(generic): we want the largest D digit number from a list of N digits
    index i0 is largest digit in the range (0..N-D) inclusive
    index i1 is largest digit in the range (i0+1..N-D+1) inclusive
    """
    total = 0
    ln = len(line)
    st, ed = 0, ln - digits
    for d in range(digits):
        idx, val = highest_digit(line, st, ed)
        total = (total * 10) + val
        st, ed = idx + 1, ed + 1
    return total


def day03a(fname):
    data = load_int_grid(fname)
    total = 0
    for line in data:
        total += high_joltage(line)
    return total


def day03b(fname):
    data = load_int_grid(fname)
    total = 0
    for line in data:
        total += high_joltage2(line, 12)
    return total


################################################################
if __name__ == "__main__":
    print("day03a", day03a("input03.txt"))
    print("day03b", day03b("input03.txt"))

################################################################


def test_high_joltage():
    assert high_joltage([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1]) == 98
    assert high_joltage([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]) == 89
    assert high_joltage([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8]) == 78
    assert high_joltage([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1]) == 92


def test_day03a():
    assert day03a("test03.txt") == 357


def test_high_joltage2():
    assert high_joltage2([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 2) == 98
    assert high_joltage2([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 2) == 89
    assert high_joltage2([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 2) == 78
    assert high_joltage2([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 2) == 92

    assert (
        high_joltage2([9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1], 12) == 987654321111
    )
    assert (
        high_joltage2([8, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9], 12) == 811111111119
    )
    assert (
        high_joltage2([2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 3, 4, 2, 7, 8], 12) == 434234234278
    )
    assert (
        high_joltage2([8, 1, 8, 1, 8, 1, 9, 1, 1, 1, 1, 2, 1, 1, 1], 12) == 888911112111
    )


def test_day03b():
    assert day03b("test03.txt") == 3121910778619

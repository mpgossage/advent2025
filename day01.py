"""
day01 should have been simple, but something messed up in the algol for part B.
It looks a lot longer than expected.
"""

import pytest
from helpers import load_lines


def day01a(fname):
    pos = 50
    result = 0
    for l in load_lines(fname):
        left = l[0] == "L"
        val = int(l[1:])
        if left:
            pos -= val
        else:
            pos += val
        if pos % 100 == 0:
            result += 1
    return result


def day01b(fname):
    pos = 50
    result = 0
    for l in load_lines(fname):
        left = l[0] == "L"
        val = int(l[1:])
        old = pos
        if left:
            if pos == 0:
                score = val // 100
            else:
                score = (100 + val - pos) // 100
            pos -= val
        else:
            pos += val
            score = pos // 100
        # print(f"old:{old} pos:{pos} l:{l} sc:{score}")
        pos = (pos + 100) % 100
        result += score
    return result


################################################################
if __name__ == "__main__":
    ##    print(parse_input("test01.txt"))
    print("day01a", day01a("input01.txt"))
    print("day01b", day01b("input01.txt"))

################################################################


def test_day01a():
    assert day01a("test01.txt") == 3


def test_day01b():
    assert day01b("test01.txt") == 6

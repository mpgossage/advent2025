"""
day02 partA looks ok, I'm a little concerned a slow string method might be too slow, lets find out.
part B takes ~ 10 seconds which is acceptable.

I could have refactored & tidied the code, but I chose to keep two completely seperate sets of code for this
"""

import pytest
from helpers import load_tokens


def is_valid_id(val):
    "simplest thing that works, slow, but might be enough"
    val = str(val)
    # odd number of digits must be valid
    lnVal = len(val)
    if lnVal % 2 == 1:
        return True
    return val[lnVal // 2 :] != val[: lnVal // 2]


def find_invalid_ids(mn, mx):
    "returns the list of invalid ids"
    result = []
    for v in range(mn, mx + 1):
        if not is_valid_id(v):
            result.append(v)
    return result


def parse_input(fname):
    result = []
    for f in load_tokens(fname, ",")[0]:
        arr = f.split("-")
        result.append((int(arr[0]), int(arr[1])))
    return result


def day02a(fname):
    data = parse_input(fname)
    total = 0
    for d in data:
        res = find_invalid_ids(d[0], d[1])
        total += sum(res)
    return total


def is_valid_id2(val):
    "modified version, now must deal with all versions"
    val = str(val)
    lnVal = len(val)
    for l in range(1, lnVal):
        if lnVal % l != 0:
            continue
        # we can break it down into chunks of length l, do they all match?
        # we can check if each chunk matches the first one
        first = val[:l]
        same = True
        # print(f"val {val} l:{l} first:{first}")
        for i in range(1, lnVal // l):
            # print(f"cmp {first} {val[i*l:(i+1)*l]}")
            if first != val[i * l : (i + 1) * l]:
                same = False
                break
        # dup found: its invalid
        if same:
            return False
    return True


def find_invalid_ids2(mn, mx):
    "returns the list of invalid ids"
    result = []
    for v in range(mn, mx + 1):
        if not is_valid_id2(v):
            result.append(v)
    return result


def day02b(fname):
    data = parse_input(fname)
    total = 0
    for d in data:
        res = find_invalid_ids2(d[0], d[1])
        total += sum(res)
    return total


################################################################
if __name__ == "__main__":
    print("day02a", day02a("input02.txt"))
    print("day02b", day02b("input02.txt"))

################################################################


def test_is_valid():
    assert is_valid_id(55) == False
    assert is_valid_id(6464) == False
    assert is_valid_id(123123) == False
    assert is_valid_id(101)


def test_find_invalid_ids():
    assert find_invalid_ids(11, 22) == [11, 22]
    assert find_invalid_ids(95, 115) == [99]
    assert find_invalid_ids(38593856, 38593862) == [38593859]


def test_is_valid2():
    assert is_valid_id2(55) == False
    assert is_valid_id2(6464) == False
    assert is_valid_id2(123123) == False
    assert is_valid_id2(101)
    assert is_valid_id2(12341234) == False
    assert is_valid_id2(123123123) == False
    assert is_valid_id2(1212121212) == False
    assert is_valid_id2(1111111) == False


def test_day02a():
    assert day02a("test02.txt") == 1227775554


def test_day02b():
    assert day02b("test02.txt") == 4174379265

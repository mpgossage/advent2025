"""
day05, fun parsing for today.
Part B might be brute forceable with a giant set, so trying that.
Move complex solution needed, build a range merging routine.
"""

import pytest
from helpers import load_lines


def parse_input(fname):
    ranges, items = [], []
    first = True  # first part is ranges
    for line in load_lines(fname):
        if first:
            if len(line) == 0:
                first = False
                continue
            rng = (int(a) for a in line.split("-"))
            ranges.append(tuple(rng))
        else:
            items.append(int(line))
    return ranges, items


def day05a(fname):
    ranges, items = parse_input(fname)
    num_fresh = 0
    for it in items:
        fresh = False
        for r1, r2 in ranges:
            if r1 <= it <= r2:
                fresh = True
                break
        if fresh:
            num_fresh += 1
    return num_fresh


def day05b_failed(fname):
    "first attempt, massive set, fails completely: Memory Error"
    ranges, _ = parse_input(fname)
    fresh = set()
    for r1, r2 in ranges:
        for i in range(r1, r2 + 1):
            fresh.add(i)
    return len(fresh)


def range_merge(a, b):
    "merges a&b and returns merged item or None if not overlapping"
    a1, a2 = a
    b1, b2 = b
    # simple if b inside a
    if a1 <= b1 <= a2 and a1 <= b2 <= a2:
        return a
    # flip logic (b in a)
    if b1 <= a1 <= b2 and b1 <= a2 <= b2:
        return b
    # partial overlap
    if a1 <= b1 <= a2 or a1 <= b2 <= a2:
        return (min(a1, b1), max(a2, b2))
    # no overlap
    return None


def day05b(fname):
    "using merge logic"
    ranges, _ = parse_input(fname)
    old_len = 0
    while old_len != len(ranges):
        old_len = len(ranges)
        # print(len(ranges),':',ranges)
        new_ranges = []
        while len(ranges) > 0:
            # get an item
            merged = ranges.pop()
            # attempt to merge with everything left
            to_remove = []
            for r in ranges:
                t = range_merge(merged, r)
                if t is not None:
                    merged = t
                    to_remove.append(r)  # will need to remove later
            # add merged item
            new_ranges.append(merged)
            # remove all items which were merged (could not remove while iterating, thats risky)
            for t in to_remove:
                ranges.remove(t)
        ranges = new_ranges
    # print("final",len(ranges),':',ranges)
    # get the total
    total = 0
    for r1, r2 in ranges:
        total += 1 + r2 - r1
    return total


################################################################
if __name__ == "__main__":
    print("day05a", day05a("input05.txt"))
    print("day05b", day05b("input05.txt"))

################################################################


def test_parse_input():
    ranges, items = parse_input("test05.txt")
    assert len(ranges) == 4
    assert len(items) == 6
    assert ranges[0] == (3, 5)
    assert ranges[3] == (12, 18)
    assert items[0] == 1
    assert items[5] == 32


def test_day05a():
    assert day05a("test05.txt") == 3


def test_day05b():
    assert day05b("test05.txt") == 14

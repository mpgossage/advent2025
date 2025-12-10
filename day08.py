"""
day08 looks like a simpler minimal spanning tree.
I'm as little concerned on the wording of the puzzle, 
the 4th join links two items which are in the same circuit. Does that count or not?
Is the next join the 4th or 5th?
Part A fails on real data due to timeout, need to optimise the find-nearest area, then it works fine.

For Part B, we need a full MST, so refactor A to extract the methods and then use it for B

"""

import pytest
import time
from helpers import load_int_tokens


def distance2(a, b):
    "returns distance squared"
    dx, dy, dz = a[0] - b[0], a[1] - b[1], a[2] - b[2]
    return dx * dx + dy * dy + dz * dz


def update_nearest_cache(data, nearest, joins):
    "updated the nearest neighbour cache"
    for i in range(len(data)):
        if nearest[i] is not None:
            continue
        # nearest distance
        n, dist = None, 1e20
        for j in range(i + 1, len(data)):
            # skip joins
            if (i, j) in joins:
                continue

            d = distance2(data[i], data[j])
            if d < dist:
                n, dist = j, d
        nearest[i] = (n, dist)


def find_nearest(nearest):
    # find nearest pair
    a, b, dist = None, None, 1e20
    for i in range(len(nearest)):
        if nearest[i][1] < dist:
            a, b, dist = i, nearest[i][0], nearest[i][1]
    return a, b


def link_nodes(a, b, circuits, nearest, joins):
    "links nodes a & b and updates all the info"
    # get the two circuits they are in right now
    find_circuit = lambda i: next(c for c in circuits if i in c)
    ca, cb = find_circuit(a), find_circuit(b)
    # add to joins
    joins.add((a, b))
    joins.add((b, a))
    # clear nearest cache
    nearest[a] = None
    nearest[b] = None
    # if a&b in not in same circuit: merge
    if ca != cb:
        # merge circuits
        circuits.remove(ca)
        circuits.remove(cb)
        circuits.append(ca | cb)


def join_items(data, num):
    "makes num joins together & returns the indexes of the joined circuits"
    datalen = len(data)

    nearest = [
        None
    ] * datalen  # nearest neighbor cache: (id, dist**2) or None for nearest neighbour
    joins = set()  # for A<=>B you can find (A,B) & (B,A)
    # all individual circuits (the logic is easier later)
    circuits = []
    for i in range(datalen):
        circuits.append(set([i]))

    start = time.time()
    for n in range(num):
        # print("step",n,"total time", time.time() - start)
        update_nearest_cache(data, nearest, joins)

        # find nearest pair
        a, b = find_nearest(nearest)

        link_nodes(a, b, circuits, nearest, joins)

    return circuits


def day08a(fname, num):
    data = load_int_tokens(fname, ",")
    circuits = join_items(data, num)
    # get the size of the circuits
    sizes = sorted(len(c) for c in circuits)
    # returns the three largest (last)
    return sizes[-1] * sizes[-2] * sizes[-3]


def day08b(fname):
    data = load_int_tokens(fname, ",")

    datalen = len(data)
    nearest = [
        None
    ] * datalen  # nearest neighbor cache: (id, dist**2) or None for nearest neighbour
    joins = set()  # for A<=>B you can find (A,B) & (B,A)
    # all individual circuits (the logic is easier later)
    circuits = []
    for i in range(datalen):
        circuits.append(set([i]))

    # until its all merged
    while len(circuits) > 1:
        update_nearest_cache(data, nearest, joins)
        a, b = find_nearest(nearest)
        link_nodes(a, b, circuits, nearest, joins)

    # last merged pair were a & b
    return data[a][0] * data[b][0]


################################################################
if __name__ == "__main__":
    print("part A", day08a("input08.txt", 1000))
    print("part B", day08b("input08.txt"))

################################################################


def test_parse_input():
    data = load_int_tokens("test08.txt", ",")
    assert len(data) == 20
    assert data[0] == [162, 817, 812]
    assert data[19] == [425, 690, 689]


def test_test_join_items():
    data = load_int_tokens("test08.txt", ",")
    result = join_items(data, 1)
    assert set([0, 19]) in result

    # 2 joins gives a 3 set
    result = join_items(data, 2)
    assert set([0, 19, 7]) in result

    # 3 joins gives a 3 set & a pair
    result = join_items(data, 3)
    assert len(result) == 17
    assert set([0, 19, 7]) in result
    assert set([2, 13]) in result

    # 4 joins gives exactly the same result as 3 joins
    result = join_items(data, 4)
    assert len(result) == 17
    assert set([0, 19, 7]) in result
    assert set([2, 13]) in result

    # 10 joins
    result = join_items(data, 10)
    print(result)
    assert len(result) == 11
    # check the lengths: a 5, a 4, two 2's, 7 1's
    clens = [len(c) for c in result]
    assert clens.count(5) == 1
    assert clens.count(4) == 1
    assert clens.count(2) == 2
    assert clens.count(1) == 7


def test_day08a():
    assert day08a("test08.txt", 10) == 40


def test_day08b():
    assert day08b("test08.txt") == 25272

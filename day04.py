"""
day04, simple grid code.
Part B needed to convert array of string to 2d array of char to allow editing, but nothing else special
"""

import pytest
from helpers import load_lines

ADJACENT = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_adjacent(grid, x, y):
    lnx, lny = len(grid[0]), len(grid)
    count = 0
    for dx, dy in ADJACENT:
        tx, ty = x + dx, y + dy
        if 0 <= tx < lnx and 0 <= ty < lny and grid[ty][tx] == "@":
            count += 1
    return count


def day04a(fname):
    grid = load_lines(fname)
    lnx, lny = len(grid[0]), len(grid)
    count = 0
    for y in range(lny):
        for x in range(lnx):
            if grid[y][x] == "@" and count_adjacent(grid, x, y) < 4:
                count += 1
    return count


def day04b(fname):
    grid = load_lines(fname)
    lnx, lny = len(grid[0]), len(grid)
    count = 0
    grid, grid_copy = [], grid
    for g in grid_copy:
        grid.append(list(g))
    # loop forever marking items to remove and removing them
    while True:
        # mark items
        to_remove = []
        for y in range(lny):
            for x in range(lnx):
                if grid[y][x] == "@" and count_adjacent(grid, x, y) < 4:
                    to_remove.append((x, y))
        # remove items
        if len(to_remove) > 0:
            count += len(to_remove)
            for x, y in to_remove:
                grid[y][x] = "."
        else:
            break
    return count


################################################################
if __name__ == "__main__":
    print("day04a", day04a("input04.txt"))
    print("day04b", day04b("input04.txt"))

################################################################


def test_count_adjacent():
    grid = load_lines("test04.txt")
    assert count_adjacent(grid, 2, 0) == 3
    assert count_adjacent(grid, 3, 0) == 3
    assert count_adjacent(grid, 5, 0) == 3
    assert count_adjacent(grid, 6, 0) == 3
    assert count_adjacent(grid, 7, 0) == 4
    assert count_adjacent(grid, 8, 0) == 3


def test_day04a():
    assert day04a("test04.txt") == 13


def test_day04b():
    assert day04b("test04.txt") == 43

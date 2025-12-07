"""
day07 looks like a simple grid.
Part B is much more complex, its a read head scratcher.
The result was computed very quickly despite it being a real big number.
"""

import pytest
from helpers import load_lines


def day07a(fname):
    grid = load_lines(fname)
    wid, hig = len(grid[0]), len(grid)
    # locate S, assume its the top line:
    sx, sy = grid[0].index("S"), 0
    todo = set([(sx, sy)])
    activated = set()
    while len(todo) > 0:
        x, y = todo.pop()
        # move beam down until it hits a splitter or it goes off the screen
        y += 1
        while y < hig:
            # split
            if grid[y][x] == "^":
                # sanity: has been found before
                if (x, y) in activated:
                    break
                activated.add((x, y))
                if x > 0:
                    todo.add((x - 1, y))
                if x < wid - 1:
                    todo.add((x + 1, y))
                break
            y += 1

    return len(activated)


def day07b(fname):
    grid = load_lines(fname)
    wid, hig = len(grid[0]), len(grid)
    # locate S, assume its the top line:
    sx, sy = grid[0].index("S"), 0
    # todo list will need to store the location & how many ways we can get there
    # but we don't need the activated list as we will be being more structured with out todo list reading
    todo = {(sx, sy): 1}
    result = 0
    while len(todo) > 0:
        # don't simply pop the first item from the list: find the smallest y value
        x, y = -1, hig
        for tx, ty in todo.keys():
            if y > ty:
                x, y = tx, ty
        # count at how many ways the beam count have some from here
        count = todo.get((x, y))
        # remove old
        del todo[(x, y)]
        # move beam down until it hits a splitter or it goes off the screen
        y += 1
        while True:
            # split
            if grid[y][x] == "^":
                # for left & right: add to times activated
                if x > 0:
                    val = todo.get((x - 1, y), 0)
                    todo[(x - 1, y)] = val + count
                if x < wid - 1:
                    val = todo.get((x + 1, y), 0)
                    todo[(x + 1, y)] = val + count
                break
            y += 1
            if y >= hig:
                # if moved off the grid, add to the result
                result += count
                break

    return result


################################################################
if __name__ == "__main__":
    print("day07a", day07a("input07.txt"))
    print("day07b", day07b("input07.txt"))

################################################################


def test_day07a():
    assert day07a("test07.txt") == 21


def test_day07b():
    assert day07b("test07.txt") == 40

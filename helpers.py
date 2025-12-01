"""
Advent of Code 2025: helpers
"""


def load_file(fname):
    with open(fname) as f:
        return f.read()


def load_lines(fname):
    with open(fname) as f:
        return [l.strip("\n") for l in f.readlines()]


def load_tokens(fname, sep=None):
    with open(fname) as f:
        return [l.strip("\n").split(sep) for l in f.readlines()]

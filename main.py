#!/usr/bin/env python

import sys


def toUpper(name: str):
    return name.capitalize()


if __name__ == "__main__":
    name = sys.argv[1]
    print(f"Hello {toUpper(name)}")

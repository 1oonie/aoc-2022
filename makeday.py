#!/usr/bin/python3

import os
import sys

default = """\
with open("{daydir}/input") as f:
    inp = f.read()

def part1():
    ...

def part2():
    ...
"""

try:
    day = int(sys.argv[1])
except:
    print("invalid day")
    sys.exit(1)

daydir = f"day{day:02}"
try:
    os.mkdir(daydir)
except:
    print("day already exists")
    sys.exit(1)

with open(f"{daydir}/input", "w") as f:
    ...

with open(f"{daydir}/main.py", "w") as f:
    f.write(default.format(daydir=daydir))

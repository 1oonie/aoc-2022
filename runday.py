#!/usr/bin/python3

import importlib
import sys

try:
    day = int(sys.argv[1])
except:
    print("invalid day")
    sys.exit(1)

daydir = f"day{day:02}"

module = importlib.import_module(f"{daydir}.main")

try:
    part = int(sys.argv[2])
except:
    print("invalid part")
    sys.exit(1)

getattr(module, f"part{part}")()
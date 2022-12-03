with open("day02/input") as f:
    inp = [l.split(" ") for l in f.read().splitlines()]

def part1():
    total = 0
    for a, b in inp:
        other, me = ord(a)-65, ord(b)-88
        total += (3 if me == other else (0 if (me + 1) % 3 == other else 6)) + me + 1

    print(total)

def part2():
    c = [1, 2, 3]

    total = 0
    for a, b in inp:
        other, res = ord(a)-65, ord(b)-88
        total += (c[(other%3)-1] if not res else ((other+1)%3+1 if res == 2 else other+1)) + res*3
    print(total)
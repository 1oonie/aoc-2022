with open("day04/input") as f:
    inp = [l.split(",") for l in f.read().splitlines()]

inc_range = lambda a, b: range(a, b+1)
zenith = lambda a: set(inc_range(*map(int, a.split("-"))))

def part1():
    total = 0
    for (a, b) in inp:
        p1, p2 = zenith(a), zenith(b)
        m = max(len(p1), len(p2))
        total += m == len(p1 | p2)
    print(total)

def part2():
    total = 0
    for (a, b) in inp:
        p1, p2 = zenith(a), zenith(b)
        total += bool(len(p1 & p2))
    print(total)
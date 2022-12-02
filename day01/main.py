with open("day01/input") as f:
    inp = f.read()

def part1():
    print(max([sum([int(f) for f in deer.split("\n") if f]) for deer in inp.split("\n\n")]))

def part2():
    print(sum(sorted([sum([int(f) for f in deer.split("\n") if f]) for deer in inp.split("\n\n")], reverse=True)[:3]))

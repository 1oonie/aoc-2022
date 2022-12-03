import string

with open("day03/input") as f:
    inp = f.read().splitlines()
    inp1 = [(l[:len(l)//2], l[len(l)//2:]) for l in inp]

def part1():
    print(sum(string.ascii_letters.index((set(a) & set(b)).pop())+1 for a, b in inp1))

def part2():
    print(sum(string.ascii_letters.index(set.intersection(*map(set, inp[i:i+3])).pop())+1 for i in range(0, len(inp), 3)))

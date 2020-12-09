def day6_pt2(lines):
    return sum([len(set.intersection(*[set(p) for p in l.split('\n')])) for l in lines])

lines = open('input.txt').read().split('\n\n')
print(day6_pt2(lines))
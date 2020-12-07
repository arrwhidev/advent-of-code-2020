from functools import reduce
from operator import mul

slopes = [
    (1,1),(3,1),(5,1),(7,1),(1,2)
]

def day3_pt2():
    f = open('input.txt')
    lines = f.read().split('\n')

    def run_slope(s):
        r,d = s
        offset = 0
        trees = 0

        for line in lines[::d]:
            if line[offset % len(line)] == '#':
                trees += 1
            offset += r
        return trees

    return reduce(mul, map(run_slope, slopes))

def test_day3_pt2():
    assert day3_pt2() == None
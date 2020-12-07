def day3():
    f = open('input.txt')
    lines = f.read().split('\n')
    r = 3
    trees = 0
    for line in lines[1::1]:
        if line[r % len(line)] == '#':
            trees += 1
        r += 3
    return trees

def test_day3():
    assert day3() == None
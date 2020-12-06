def day1():
    f = open('input.txt')
    entries = f.readlines()

    for i in entries:
        for j in entries:
            for k in entries:
                if int(i) + int(j) + int(k) == 2020:
                    return int(i) * int(j) * int(k)

def test_day1():
    assert day1() == None
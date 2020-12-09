def day5(lines):
    r = str.maketrans('FBLR','0101')
    return max([int(l.translate(r), 2) for l in lines])

lines = open('input.txt').readlines()
print(day5(lines))
def day5_pt2(lines):
    r = str.maketrans('FBLR','0101')
    seats = sorted([int(l.translate(r), 2) for l in lines])
    for n in range(0, len(seats)):
        if seats[n]+1 != seats[n+1]:
            return seats[n]+1

lines = open('input.txt').readlines()
print(day5_pt2(lines))
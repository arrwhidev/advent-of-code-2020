def day6(lines):
    return sum([len(set(line.replace('\n',''))) for line in lines])

lines = open('input.txt').read().split('\n\n')
print(day6(lines))
import re

def strip(s):
    return re.sub('[^a-zA-Z]+', '', s).replace('bags','').replace('bag','')

def day7(lines, q):
    contained = {}
    for line in lines:
        outer, inner = line.split('contain')
        for inner in [strip(b) for b in inner.split(', ')]:
            contained.setdefault(inner,[]).append(strip(outer))
    
    bags = set()
    def scan(q):
        for c in contained.get(q, []):
            bags.add(c)
            scan(c)

    scan(q)
    return len(bags)

lines = open('input.txt').read().split('\n')
print(day7(lines, 'shinygold'))
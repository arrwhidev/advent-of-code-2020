import re

def strip(s):
    return re.sub(r'[^\d\w]+', '', s.replace('bags','').replace('bag',''))

def split(s):
    return re.findall(r'(\d+)?(\w+)', strip(s))[0]

def day7(lines, q):
    contains={} 
    for line in lines:
        bag, bags = line.split('contain')
        bag = strip(bag)
        contains[bag] = [split(b) for b in bags.split(', ')]
    
    def scan(q):
        total = 0
        for n, c in contains.get(q, []):
            n = int(n if n != '' else '0')
            total += n + (n * scan(c))
        return total
    
    return scan(q)

lines = open('input.txt').read().split('\n')
print(day7(lines, 'shinygold'))

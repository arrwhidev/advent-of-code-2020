required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def is_valid(passport):
    return all(k in passport for k in required)

def line_to_dic(line):
    pairs = [ p.split(':') for p in line.replace('\n', ' ').split(' ') ]
    return { k:v for (k,v) in pairs }

def to_passports(lines):
    return [ line_to_dic(line) for line in lines ]

def day4():
    f = open('input.txt')
    passports = to_passports(f.read().split('\n\n'))
    return len(list(filter(is_valid, passports)))

def test_day4():
    assert day4() == 210
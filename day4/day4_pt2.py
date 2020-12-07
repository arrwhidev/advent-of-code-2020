import re

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

def byr(passport):
    return len(passport['byr']) == 4 and int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002

def iyr(passport):
    return len(passport['iyr']) == 4 and int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020

def eyr(passport):
    return len(passport['eyr']) == 4 and int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030

def hgt(passport):
    if passport['hgt'].endswith('cm'):
        n = int(re.sub('[^0-9]', '', passport['hgt']))
        return n >= 150 and n <= 193
    elif passport['hgt'].endswith('in'):
        n = int(re.sub('[^0-9]', '', passport['hgt']))
        return n >= 59 and n <= 76
    else:
        return False

def hcl(passport):
    return re.search('[#][0-9a-f]{1,6}$', passport['hcl'])

def ecl(passport):
    return passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(passport):
    return len(passport['pid']) == 9

def is_valid(passport):
    return all(k in passport for k in required) and byr(passport) and iyr(passport) and eyr(passport) and hgt(passport) and hcl(passport) and ecl(passport) and pid(passport)

def line_to_dic(line):
    pairs = [ p.split(':') for p in line.replace('\n', ' ').split(' ') ]
    return { k:v for (k,v) in pairs }

def to_passports(lines):
    return [ line_to_dic(line) for line in lines ]

def day4_pt2():
    f = open('input.txt')
    passports = to_passports(f.read().split('\n\n'))
    return len(list(filter(is_valid, passports)))

def test_day4_pt2():
    assert day4_pt2() is None
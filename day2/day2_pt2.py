def split_policy(policy):
    x, char = policy.split(' ')
    min, max = x.split('-')
    return (int(min), int(max), char)

def day2_pt2():
    f = open('input.txt')
    entries = f.read().split('\n')
    good_paswords = 0
    
    for e in entries:
        if len(e) > 0:
            policy, password = e.split(': ')
            min, max, char = split_policy(policy)
            matches = 0

            if len(password) >= min and password[min-1] == char:
                matches += 1

            if len(password) >= max and password[max-1] == char:
                matches += 1

            if matches == 1:   
                good_paswords += 1

    return good_paswords

def test_day2_pt2():
    assert day2_pt2() == 502
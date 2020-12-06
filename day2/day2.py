def split_policy(policy):
    x, char = policy.split(' ')
    min, max = x.split('-')
    return (int(min), int(max), char)

def day2():
    f = open('input.txt')
    entries = f.read().split('\n')
    good_paswords = 0

    for e in entries:
        if len(e) > 0:
            policy, password = e.split(': ')
            min, max, char = split_policy(policy)
            cnt = password.count(char)
            if cnt >= min and cnt <= max:
                good_paswords += 1

    return good_paswords

def test_day2():
    assert day2() == None
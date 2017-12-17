def equal(a, b):
    if a == b:
        return int(a)
    else:
        return 0

assert equal("1", "1") == 1
assert equal("1", "2") == 0

def sum_captcha(string, step=1):
    c_string = string[:] + string[0:step]
    return sum(equal(c_string[i], c_string[i+step]) for i in range(len(c_string)-step))

assert sum_captcha('1122') == 3
assert sum_captcha('1111') == 4
assert sum_captcha('91212129') == 9

dat = open("./data/day1.txt").readlines()
dat1 = dat[0].strip()
print("q1: {}".format(sum_captcha(dat1)))

assert sum_captcha('1212', 2) == 6
assert sum_captcha('1221', 2) == 0
assert sum_captcha('12131415', 2) == 4

dat2 = dat[1].strip()
print("q2: {}".format(sum_captcha(dat2, len(dat2)//2)))




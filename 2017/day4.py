dat1 = open("./data/day4_1.txt")

def vaild(phrase):
    tmp = phrase.strip().split()
    return 1 if len(set(tmp)) == len(tmp) else 0

assert vaild("aa bb cc dd ee") == 1
assert vaild("aa bb cc dd aa") == 0
assert vaild("aa bb cc dd aaa") == 1

print("q1: {}".format(sum(vaild(line) for line in dat1)))

def vaild2(phrase):
    tmp = ["".join(sorted(i)) for i in phrase.strip().split()]
    return 1 if len(set(tmp)) == len(tmp) else 0

dat2 = open("./data/day4_2.txt")
assert vaild2("abcde fghij") == 1
assert vaild2("abcde xyz ecdab") == 0
assert vaild2("a ab abc abd abf abj") == 1

print("q2: {}".format(sum(vaild2(line) for line in dat2)))

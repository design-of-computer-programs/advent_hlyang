def diff(line):
    tmp = [int(i) for i in line]
    return max(tmp) - min(tmp)

def div(line):
    tmp = [int(i) for i in line]
    for i in range(len(tmp)):
        for j in range(len(tmp)):
            if i != j and tmp[j] % tmp[i] == 0:
                # print(tmp[i], tmp[j])
                return tmp[j] // tmp[i]

dat1 = open("./data/day2_1.txt")
print("q1: {}".format(sum(diff(line.strip().split()) for line in dat1)))

assert div("5 9 2 8".split()) == 4
assert div("9 4 7 3".split()) == 3

dat2 = open("./data/day2_2.txt")
print("q2: {}".format(sum(div(line.strip().split()) for line in dat2)))


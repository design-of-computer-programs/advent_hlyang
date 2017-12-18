def move(my_list, threshold=3, q=1):
    steps = 0
    next_step = 0
    while True:
        if (q==1) or (my_list[next_step] < threshold):
            my_list[next_step] += 1
            next_step += my_list[next_step] - 1
        else:
            my_list[next_step] -= 1
            next_step += my_list[next_step] + 1
        steps += 1
        # print(my_list, next_step, steps)
        if (next_step > len(my_list) - 1) or (next_step < 0):
            break
    return steps

assert move([0, 3, 0, 1, -3]) == 5
assert move([0, 3, 0, 1, -3], q=2) == 10

dat = open("./data/day5.txt")
my_list = [int(line) for line in dat]
print("q1: {}".format(move(my_list)))

# bc question one changed my_list
dat.seek(0)
my_list = [int(line) for line in dat]
print("q2: {}".format(move(my_list, q=2)))

dat.close()

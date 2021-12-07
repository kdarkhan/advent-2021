from statistics import mode

input = 'day7.txt'


def do_stuff():

    with open(input) as f:
        s = [int(x) for x in f.readline().strip().split(',')]
        x = mode(s)

        print(sum([abs(i - x - 1) for i in s]))

        best = sum([abs(i - x) for i in s])
        for d in range(1000):
            best = min(best, sum([abs(i - x - d) for i in s]))

        print(best)


do_stuff()

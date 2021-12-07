input = 'day7.txt'


def do_stuff():

    with open(input) as f:
        s = [int(x) for x in f.readline().strip().split(',')]
        m = max(s)

        best = -1

        for i in range(m):
            cur = 0
            for n in s:
                cur += abs(i - n) * (abs(i - n) + 1) // 2

            best = cur if best == -1 else min(best, cur)
        print(best)


do_stuff()

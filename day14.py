from collections import defaultdict, Counter
import sys

def solve():
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.readlines()]

        input = lines[0]

        lines = [tuple(i for i in x.split(' -> ')) for x in lines[2:]]

        d = defaultdict(lambda: 0)

        cnts = Counter(c for c in input)

        for i in range(len(input) - 1):
            d[input[i:i+2]] += 1
        print(d)


        for i in range(10):
            nxt = defaultdict(lambda: 0)
            for (a1, a2) in lines:
                if d[a1] > 0:
                    nxt[a1[0] + a2] += d[a1]
                    nxt[a2 + a1[1]] += d[a1]
                    cnts[a2] += d[a1]
                    del d[a1]

            for key, value in nxt.items():
                # print(key, value, d[key])
                d[key] += value

        print(d)
        small = min([x for x in cnts.values() if x > 0])
        large = max([x for x in cnts.values()])
        print(large, small, large - small)


        # print(input)
        # print(lines)
solve()

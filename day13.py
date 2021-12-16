from collections import defaultdict, Counter
import sys

def solve():
    with open(sys.argv[1]) as f:
        coords = []
        instructions = []
        seen_space = False
        mx, my = 0, 0
        for line in f:
            line = line.strip()
            if not line:
                seen_space = True
            elif seen_space:
                instructions.append(line.split()[2])
            else:
                x, y = tuple(int(x) for x in line.split(','))
                mx = max(x, mx)
                my = max(y, my)
                coords.append((x, y))

    print(instructions)

    axis, dist = instructions[0].split('=')
    dist = int(dist)

    nxt = []
    for x, y in coords:
        if axis == 'x':
            if x > dist:
                if dist * 2 >= x:
                    nxt.append((2 * dist - x, y))
                else:
                    nxt.append((dist - x, y))
            else:
                nxt.append((x, y))
        else:
            if y > dist:
                if dist * 2 >= y:
                    nxt.append((x, 2 * dist - y))
                else:
                    nxt.append((x, dist - y))
            else:
                nxt.append((x, y))


    print(nxt)
    print(len(set(nxt)))


solve()

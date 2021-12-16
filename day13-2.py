import sys

def print_coords(coords):
    mx, my = 0, 0
    for x, y in coords:
        mx = max(mx, x)
        my = max(my, y)
    print(mx, my)

    coords = set(coords)

    for i in range(my + 1):
        line = ''.join(['#' if (j, i) in coords else ' ' for j in range(mx + 1)])
        print(line)

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

    nxt = []

    for instruction in instructions:
        axis, dist = instruction.split('=')
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
        coords = nxt


    # print(nxt)
    print(len(set(nxt)))
    print_coords(nxt)


solve()

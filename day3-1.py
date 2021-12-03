with open('day3.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    again = lines[:]
    print('start', lines)


    idx = 0
    while len(lines) > 1:
        nums = [l[idx] for l in lines]
        cnt = sum([int(l[idx]) for l in lines])
        common = '1' if len(lines) / 2 <= cnt else '0'

        lines = list(filter(lambda x: x[idx] == common, lines))
        idx += 1

    a = int(lines[0], 2)
    lines = again


    idx = 0
    while len(lines) > 1:
        nums = [l[idx] for l in lines]
        cnt = sum([int(l[idx]) for l in lines])
        common = '1' if len(lines) / 2 > cnt else '0'

        lines = list(filter(lambda x: x[idx] == common, lines))
        idx += 1
    b = int(lines[0], 2)
    print(a * b)

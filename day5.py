input = 'day5.txt'


def do_stuff():
    lines = []
    m_x, m_y = 0, 0

    with open(input) as f:
        for line in f:
            pairs = line.strip().split(' -> ')
            x0, y0 = [int(x) for x in pairs[0].split(',')]
            x1, y1 = [int(x) for x in pairs[1].split(',')]

            lines.append(((x0, y0), (x1, y1)))

            m_x = max(m_x, x0 + 1)
            m_y = max(m_y, y0 + 1)
    print(lines)
    print(m_x, m_y)
    grid = [[0] * m_y for i in range(m_x)]

    for (x0, y0), (x1, y1) in lines:
        print(x0, y0, x1, y1)

        if x0 == x1:
            if y0 > y1:
                y0, y1 = y1, y0
            for i in range(y0, y1 + 1):
                grid[x0][i] += 1

        elif y0 == y1:
            if x0 > x1:
                x0, x1 = x1, x0
            for i in range(x0, x1 + 1):
                grid[i][y0] += 1

    cnt = 0
    for line in grid:
        for j in line:
            if j > 1:
                cnt += 1
    print(cnt)


print(do_stuff())

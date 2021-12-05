import re

input = 'day5.txt'

def print_board(board):
    print('---------------------------------')
    for l in board:
        print(l)
    print('---------------------------------')

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
        elif abs(x0 - x1) == abs(y0 - y1):
            xs = 1 if x0 < x1 else -1
            ys = 1 if y0 < y1 else -1

            for i in range(0, abs(x0 - x1) + 1):
                grid[x0 + i * xs][y0 + i * ys] += 1

    cnt = 0
    for l in grid:
        for j in l:
            if j > 1:
                cnt += 1

    print_board(grid)
    print(cnt)

print(do_stuff())

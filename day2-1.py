with open('day2.txt', 'r') as f:
    x, y, aim = 0, 0, 0
    for line in f:
        dir, cnt = line.split(' ')
        cnt = int(cnt)
        if dir == 'forward':
            x += cnt
            y += aim * cnt
        elif dir == 'down':
            aim += cnt
        else:
            aim -= cnt
        print('dirs is ', dir, cnt)
        print('x,y,aim ', x,y,aim)
    print(x * y)

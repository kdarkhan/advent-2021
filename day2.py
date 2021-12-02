with open('day2.txt', 'r') as f:
    x, y = 0, 0
    for line in f:
        dir, cnt = line.split(' ')
        cnt = int(cnt)
        if dir == 'forward':
            x += cnt
        elif dir == 'down':
            y += cnt
        else:
            y -= cnt
    print(x * y)

with open('day1.txt', 'r') as f:
    prev = -1
    cnt = 0
    sum = 0
    s0, s1, s2 = 0, 0, 0
    for i, line in enumerate(f):
        num = int(line.strip())
        nsum = sum - s0 + num
        if i > 2 and nsum > sum:
            cnt += 1
        sum = nsum
        s0, s1, s2 = s1, s2, num
    print(cnt)

print('hello')
with open('day1.txt', 'r') as f:
    prev = -1
    cnt = 0
    for line in f:
        num = int(line.strip())
        if prev != -1 and prev < num:
            cnt += 1
        prev = num
    print(cnt)

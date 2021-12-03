with open('day3.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    cnts = [0] * len(lines[0])

    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                cnts[i] += 1
    bits = ['1' if cnts[i] > len(lines) / 2 else '0' for i in range(len(lines[0]))]
    flip = ['0' if cnts[i] > len(lines) / 2 else '1' for i in range(len(lines[0]))]
    a = int(''.join(bits), 2)
    b = int(''.join(flip), 2)
    print(a*b)

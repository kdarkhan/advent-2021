import heapq
import sys

def solve():
    with open(sys.argv[1]) as f:
        initial_lines = [x.strip() for x in f.readlines()]

        initial_lines = [[int(i) for i in x] for x in initial_lines]

        wi, hi = len(initial_lines[0]), len(initial_lines)

        lines = [[0] * hi * 5 for x in range(wi * 5)]


        for i in range(hi):
            for j in range(wi):
                lines[i][j] = initial_lines[i][j]

        for i in range(hi):
            for j in range(wi, wi * 5):
                nxt = lines[i][j - wi] + 1
                if nxt > 9:
                    nxt = 1
                lines[i][j] = nxt

        for i in range(hi, hi * 5):
            for j in range(wi * 5):
                nxt = lines[i - hi][j] + 1
                if nxt > 9:
                    nxt = 1
                lines[i][j] = nxt

        x, y = 0, 0
        w, h = len(lines[0]), len(lines)
        tx, ty = h - 1, w - 1

        dist = [[-1] * w for x in range(h)]

        dist[0][0] = 0

        hp = [(0, (0, 0))]

        while hp:
            _, (cx, cy) = heapq.heappop(hp)

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if nx >= 0 and nx < h and ny >= 0 and ny < w:
                    if dist[nx][ny] == -1:
                        heapq.heappush(hp, (lines[nx][ny] + dist[cx][cy], (nx, ny)))
                        dist[nx][ny] = lines[nx][ny] + dist[cx][cy]
                    else:
                        dist[nx][ny] = min(lines[nx][ny] + dist[cx][cy], dist[nx][ny])

                    if nx == tx and ny == ty:
                        print('found it', dist[nx][ny])
                        return

solve()

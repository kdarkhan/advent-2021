import heapq
import sys

def solve():
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.readlines()]

        lines = [[int(i) for i in x] for x in lines]

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

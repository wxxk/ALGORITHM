from collections import deque
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]

dy = [-1, 1, 0, 0]
dz = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 0))
visited[0][0][0] = 1

while queue:
    x, y, z = queue.popleft()

    if y == n - 1 and z == m - 1:
        print(visited[x][y][z])
        break

    for i in range(4):
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= ny < n and 0 <= nz < m:
            # 0인경우 그냥 이동
            if matrix[ny][nz] == 0 and not visited[x][ny][nz]:
                visited[x][ny][nz] = visited[x][y][z] + 1
                queue.append((x, ny, nz))

            # 1인 경우 벽을 뚫고 이동
            elif x == 0 and matrix[ny][nz] == 1 and not visited[x + 1][ny][nz]:
                visited[1][ny][nz] = visited[0][y][z] + 1
                queue.append((1, ny, nz))

else:
    print(-1)

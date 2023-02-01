from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m, t = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
print(visited)
queue = deque()
queue.append((0, 0, 0))
dy = [-1, 1, 0, 0]
dz = [0, 0, -1, 1]

while queue:
    x, y, z = queue.popleft()

    if y == n - 1 and z == m - 1:
        if visited[x][y][z] <= t:
            print(visited[x][y][z])
            break
        else:
            print("Fail")
            break

    for i in range(4):
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= ny < n and 0 <= nz < m:
            if x == 1 and not visited[x][ny][nz]:
                visited[x][ny][nz] = visited[x][y][z] + 1
                queue.append((x, ny, nz))
            elif x == 0 and not visited[x + 1][ny][nz] and matrix[ny][nz] == 2:
                visited[1][ny][nz] = visited[x][y][z] + 1
                queue.append((1, ny, nz))
            elif x == 0 and not visited[x][ny][nz] and matrix[ny][nz] == 0:
                visited[x][ny][nz] = visited[x][y][z] + 1
                queue.append((x, ny, nz))
else:
    print("Fail")

from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs():
    q = deque()
    q.append((sz, sy, sx))
    visited[sz][sy][sx] = 0

    while q:
        cz, cy, cx = q.popleft()

        for i in range(6):
            nz = cz + dz[i]
            ny = cy + dy[i]
            nx = cx + dx[i]

            if (
                0 <= nz < l
                and 0 <= ny < r
                and 0 <= nx < c
                and visited[nz][ny][nx] == -1
            ):
                if matrix[nz][ny][nx] == "." or matrix[nz][ny][nx] == "E":
                    visited[nz][ny][nx] = visited[cz][cy][cx] + 1
                    q.append((nz, ny, nx))


dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    matrix = [[] * r for _ in range(l)]
    for i in range(l):
        for j in range(r):
            matrix[i].append(list(map(str, input().strip())))
        input()
    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if matrix[z][y][x] == "S":
                    sz, sy, sx = z, y, x
                if matrix[z][y][x] == "E":
                    ez, ey, ex = z, y, x
    bfs()
    print(
        "Trapped!"
        if visited[ez][ey][ex] == -1
        else f"Escaped in {visited[ez][ey][ex]} minute(s)."
    )

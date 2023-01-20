from collections import deque
import sys

sys.stdin = open("input.txt")

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())

for t in range(T):

    i = int(input())

    matrix = [[0] * i for _ in range(i)]
    visited = [[False] * i for _ in range(i)]
    queue = deque()
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    visited[sx][sy] = True
    queue.append((sx, sy, 0))

    while queue:
        a, b, cnt = queue.popleft()
        if (a, b) == (ex, ey):
            print(cnt)
            break

        for x in range(8):
            nx = a + dx[x]
            ny = b + dy[x]

            if 0 <= nx < i and 0 <= ny < i and not visited[nx][ny]:
                # pprint(visited)
                visited[nx][ny] = True
                queue.append((nx, ny, cnt + 1))

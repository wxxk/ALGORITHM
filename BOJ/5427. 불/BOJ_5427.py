from collections import deque
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

w, h = map(int, input().split())
matrix = [list(input().strip()) for _ in range(h)]
visited = [[False] * w for _ in range(h)]

fire = deque()
person = deque()

for i in range(h):
    for j in range(w):
        if matrix[i][j] == "*":
            fire.append((i, j))

        elif matrix[i][j] == "@":
            person.append((i, j, 1))


while fire and person:
    fh, fw = fire.popleft()
    ph, pw, cnt = person.popleft()
    visited[fh][fw], visited[ph][pw] = True, True

    if ph == (h - 1) or pw == (w - 1):
        print(cnt)
        break

    for i in range(4):
        fx, fy = fh + dx[i], fw + dy[i]
        px, py = ph + dx[i], pw + dy[i]

        if 0 <= fx < h and 0 <= fy < w:
            if not visited[fx][fy] and matrix[fx][fy] != "#":
                visited[fx][fy] = True
                matrix[fx][fy] = "*"
                fire.append((fx, fy))

        if 0 <= px < h and 0 < py < w:
            if not visited[px][py] and matrix[px][py] == ".":
                visited[px][py] = True
                matrix[px][py] = "@"
                person.append((px, py, cnt + 1))

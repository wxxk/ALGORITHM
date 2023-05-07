import sys
import copy

# sys.stdin = open("input.txt")
input = sys.stdin.readline
from collections import deque


# 벽 세우기
# 바이러스 퍼뜨리기
# 영역 크기 구하기
def bfs():
    tmp_matrix = copy.deepcopy(matrix)
    q = deque()

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if tmp_matrix[nx][ny] == 0:
                    tmp_matrix[nx][ny] = 2
                    q.append((nx, ny))

    global answer
    cnt = 0
    for i in tmp_matrix:
        cnt += i.count(0)

    answer = max(answer, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][j] = 1
                wall(cnt + 1)
                matrix[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]
answer = 0
wall(0)

print(answer)

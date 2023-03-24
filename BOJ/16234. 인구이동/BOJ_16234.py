from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    union = [(x, y)]  # 연합에 속하는 국가들의 좌표를 담은 리스트
    total_pop = matrix[x][y]  # 연합 내 모든 국가의 인구 수의 합
    visited[x][y] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    diff = abs(matrix[x][y] - matrix[nx][ny])  # 두 지점의 인구 차이
                    if l <= diff <= r:  # 인구 차이가 l 이상 r 이하인 경우
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        union.append((nx, ny))
                        total_pop += matrix[nx][ny]
    return union, total_pop


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

answer = 0
while True:
    visited = [[False] * n for _ in range(n)]
    unions = []  # 연합 정보를 담은 리스트
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union, total_pop = bfs(i, j, visited)
                if len(union) > 1:  # 연합 국가가 2개 이상인 경우
                    unions.append((union, total_pop))

    if not unions:
        break

    for union, total_pop in unions:
        avg_pop = total_pop // len(union)  # 연합 내 국가들의 인구 수의 평균

        for x, y in union:
            matrix[x][y] = avg_pop

    answer += 1  # 인구 이동이 이루어진 횟수 증가

print(answer)

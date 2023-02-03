from heapq import heappop, heappush
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 1  # test case

while True:
    n = int(input())
    if n == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[INF] * n for _ in range(n)]
    heap = []
    heappush(heap, (matrix[0][0], 0, 0))  # 시작시점 비용, 시작지점 좌표
    visited[0][0] = matrix[0][0]  # visited에 비용

    while heap:
        cost, x, y = heappop(heap)

        # 종료 조건
        if x == n - 1 and y == n - 1:
            print(f"Problem {cnt}: {cost}")
            break

        if cost > visited[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + matrix[nx][ny]  # 해당 노드를 거쳐 갈 떄 처리

                if visited[nx][ny] > next_cost:  # 알고 있는 거리보다 작으면 갱신
                    visited[nx][ny] = next_cost  # 다음 거리 계산
                    heappush(heap, (next_cost, nx, ny))
    cnt += 1

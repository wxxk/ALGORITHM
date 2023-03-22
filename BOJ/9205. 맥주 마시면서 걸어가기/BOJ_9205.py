from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def bfs(start, end, dis, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        cur = q.popleft()

        if cur == end:
            return True

        for i in range(len(dis)):
            if not visited[i] and dis[cur][i] <= 1000:
                q.append(i)
                visited[i] = True
    return False


t = int(input())

for _ in range(t):
    n = int(input())  # 맥주를 파는 편의점 개수

    locations = []  # 집, 편의점, 페스티벌 좌표를 저장할 리스트
    for i in range(n + 2):
        x, y = map(int, input().split())
        locations.append((x, y))

    # 모든 좌표 쌍 사이의 거리를 계산하여 저장
    dis = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            temp = abs(locations[i][0] - locations[j][0]) + abs(
                locations[i][1] - locations[j][1]
            )
            dis[i][j] = temp
            dis[j][i] = temp

    # 너비 우선 탐색
    visited = [False] * (n + 2)
    if bfs(0, n + 1, dis, visited):
        print("happy")
    else:
        print("sad")

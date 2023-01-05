import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)


def DFS(v):
    global count
    visited[v] = count  # 도는 순서 기록
    for i in matrix[v]:
        if visited[i] == 0:
            count += 1
            DFS(i)


# 인풋
n, m, r = map(int, sys.stdin.readline().split())
matrix = [[] for i in range(n + 1)]
# 방문리스트
visited = [0] * (n + 1)
# 카운트
count = 1

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

for i in matrix:
    i.sort()

DFS(r)

for j in range(1, n + 1):
    print(visited[j])

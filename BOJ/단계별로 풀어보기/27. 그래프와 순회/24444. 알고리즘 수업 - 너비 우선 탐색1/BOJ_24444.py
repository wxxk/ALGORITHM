import sys
from collections import deque

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def BFS(v):
    global cnt
    visited[v] = cnt
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for i in matrix[v]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)


n, m, r = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

for i in matrix:
    i.sort()

BFS(r)

for j in range(1, len(visited)):
    print(visited[j])

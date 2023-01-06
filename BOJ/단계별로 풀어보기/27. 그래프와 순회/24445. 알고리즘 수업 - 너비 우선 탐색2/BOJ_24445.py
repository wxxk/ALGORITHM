import sys
from collections import deque

sys.setrecursionlimit(10**6)
sys.stdin = open("input.txt")


def BFS(v):
    global cnt
    visited[v] = cnt
    queue = deque([v])

    while queue:
        v = queue.popleft()
        for j in matrix[v]:
            if visited[j] == 0:
                cnt += 1
                visited[j] = cnt
                queue.append(j)


input = sys.stdin.readline
n, m, r = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

for i in matrix:
    i.sort(reverse=True)

BFS(r)

for k in range(1, len(visited)):
    print(visited[k])

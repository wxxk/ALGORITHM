import sys

sys.stdin = open("input.txt")
sys.setrecursionlimit(10**6)


def DFS(v):
    global cnt
    visited[v] = cnt
    for i in matrix[v]:
        if visited[i] == 0:
            cnt += 1
            DFS(i)


input = sys.stdin.readline
n, m, r = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 1

for i in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

for j in matrix:
    j.sort(reverse=True)

DFS(r)

for k in range(1, n + 1):
    print(visited[k])

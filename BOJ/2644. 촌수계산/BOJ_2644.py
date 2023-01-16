import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(v, cnt):
    visited[v] = True
    cnt += 1

    if v == b:
        result.append(cnt)

    for i in matrix[v]:
        if not visited[i]:
            dfs(i, cnt)


n = int(input())
a, b = map(int, input().split())
m = int(input())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for i in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

dfs(a, 0)

if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)

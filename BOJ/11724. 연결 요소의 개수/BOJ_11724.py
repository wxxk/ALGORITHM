import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline


def DFS(v):
    stack = [v]
    visited[v] = True

    while stack:
        cur = stack.pop()
        for adj in matrix[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)


n, m = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)

for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        DFS(i)
print(count)

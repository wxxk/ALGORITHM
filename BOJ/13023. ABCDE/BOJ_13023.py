import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def dfs(start, cnt):
    global answer

    visited[start] = True

    if cnt == 4:
        answer = True
        return

    for i in matrix[start]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False


n, m = map(int, input().split())
matrix = [[] for _ in range(n)]
visited = [False] * 2001
answer = False

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)


for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if answer:
        break

if not answer:
    print(0)
else:
    print(1)

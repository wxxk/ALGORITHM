import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def back(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            res.append(num[i])
            back(i)
            visited[i] = False
            res.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False] * n
res = []

back(1)

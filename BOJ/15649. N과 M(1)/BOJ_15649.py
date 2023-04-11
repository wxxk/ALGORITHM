import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
res = []
visited = [False] * (n + 1)

""" 중복 없이 M개를 고른 수열"""


def back(start):
    if len(res) == m:
        print(*res)

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            back(i)
            visited[i] = False
            res.pop()


back(1)

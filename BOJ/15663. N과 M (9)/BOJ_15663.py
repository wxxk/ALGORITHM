import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [False] * n
num = sorted(list(map(int, input().split())))
res = []


def back(start):
    if len(res) == m:
        print(*res)
        return

    temp = 0
    for i in range(n):
        if not visited[i] and temp != num[i]:
            visited[i] = True
            res.append(num[i])
            temp = num[i]
            back(i)
            visited[i] = False
            res.pop()


back(1)

import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def back(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(1, n + 1):
        # if not visited[i]:
        # visited[i] = True
        res.append(num[i - 1])
        back(i)
        # visited[i] = False
        res.pop()


n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
# visited = [False] * (n+1)
res = []

back(1)

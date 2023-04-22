import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def back(start):
    global cnt

    if res and sum(res) == s:
        cnt += 1

    for i in range(start, n):
        if not visited[i]:
            visited[i] = True
            res.append(num[i])
            back(i + 1)
            visited[i] = False
            res.pop()


n, s = map(int, input().split())
num = list(map(int, input().split()))
visited = [False] * n
res = []
cnt = 0
back(0)

print(cnt)

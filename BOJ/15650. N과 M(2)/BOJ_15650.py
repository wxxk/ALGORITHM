import sys

input = sys.stdin.readline

n, m = map(int, input().split())
res = []
visited = [False] * (n + 1)

# 중복 없이 M개를 고른 수열
def back_1(start):
    if len(res) == m:
        print(*res)

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            back_1(i)
            visited[i] = False
            res.pop()


# 오름차순
def back_2(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = True
            res.append(i)
            back_2(i + 1)
            visited[i] = False
            res.pop()


back_2(1)

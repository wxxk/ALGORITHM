import sys

# sys.stdin = open('input.txt')
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


# 사전 순으로 증가
def back_3(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(1, n + 1):
        visited[i] = True
        res.append(i)
        back_3(i)
        visited[i] = False
        res.pop()


# 비내림차순
def back_4(start):
    if len(res) == m:
        print(*res)
        return

    for i in range(start, n + 1):
        # visited[i] = True
        res.append(i)
        back_4(i)
        # visited[i] = False
        res.pop()


back_4(1)

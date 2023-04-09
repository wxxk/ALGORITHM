import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def back(arr, index):
    if len(arr) == m:
        print(*arr)
        return

    for i in range(index, n):
        if not visited[i]:
            visited[i] = True
            arr.append(num[i])
            back(arr, i + 1)
            visited[i] = False
            arr.pop()


n, m = map(int, input().split())
visited = [False for _ in range(n)]
num = [i for i in range(1, n + 1)]

back([], 0)

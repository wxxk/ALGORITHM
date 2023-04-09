import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))

        return

    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            back()
            ans.pop()


# n = n까지 // m개의 수
n, m = map(int, input().split())
ans = []

back()

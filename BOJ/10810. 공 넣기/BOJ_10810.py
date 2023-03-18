import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
stack = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    i -= 1
    j -= 1

    for num in range(i, j + 1):
        stack[num] = k

print(*stack)

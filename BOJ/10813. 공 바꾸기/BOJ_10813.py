import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
stack = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    stack[i], stack[j] = stack[j], stack[i]

print(*stack)

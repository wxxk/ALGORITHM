import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * i)

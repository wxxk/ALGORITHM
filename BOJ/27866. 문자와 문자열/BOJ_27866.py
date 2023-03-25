import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

s = list(input())
n = int(input())
print(s[n - 1])

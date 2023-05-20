import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

num = sorted(list(map(int, input().split())))
print(*num)

import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    word = input().strip()
    print(word[0] + word[-1])

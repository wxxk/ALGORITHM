import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

nums = map(int, input().split())
answer = 0
for i in nums:
    answer += i * i

print(answer % 10)

import sys

sys.stdin = open("input.txt")

n = int(input())
num = list(map(int, input().split()))
result = 0


for i in range(len(num) - 1):
    for j in range(i, -1, -1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]

# 배열의 합 구하기
for i in range(1, len(num) + 1):
    print(num[:i])

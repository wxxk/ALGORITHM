import sys

sys.stdin = open("input.txt")

n = int(input())  # 수의 개수
bubble = []

for i in range(n):
    bubble.append(int(input()))

for i in range(n - 1):
    for j in range(n - 1 - i):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

for i in range(len(bubble)):
    print(bubble[i])

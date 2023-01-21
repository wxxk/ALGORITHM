import sys

sys.stdin = open("input.txt")
from collections import deque

n, k = map(int, input().split())
numbers = deque()
answer = []

for i in range(1, n + 1):
    numbers.append(i)

while numbers:
    for j in range(k - 1):
        numbers.append(numbers.popleft())
    answer.append(numbers.popleft())

print("<", end="")
for i in range(len(answer) - 1):
    print("%d, " % answer[i], end="")

print(answer[-1], end="")
print(">", end="")
# print(answer)

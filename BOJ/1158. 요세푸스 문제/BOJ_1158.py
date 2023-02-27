from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
people = deque(i for i in range(1, n + 1))
result = []
cnt = 0

while True:

    if not people:
        break

    if k - 1 > cnt:
        people.append(people.popleft())
        cnt += 1
    else:
        result.append(people.popleft())
        cnt = 0

print("<", ", ".join(map(str, result)), ">", sep="")

import sys
from itertools import combinations

input = sys.stdin.readline

a = input().strip()
answer = set()
stack = []
temp = []

for idx, word in enumerate(list(a)):
    if word == "(":
        stack.append(idx)
    elif word == ")":
        start = stack.pop()
        end = idx
        temp.append([start, end])

for i in range(1, len(temp) + 1):
    com = combinations(temp, i)

    for c in com:
        temp_a = list(a)

        for j in c:
            start, end = j
            temp_a[start] = ""
            temp_a[end] = ""

        answer.add("".join(temp_a))

for a in sorted(answer):
    print(a)

import sys
sys.stdin = open('10773.txt')

import sys
N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

print(sum(stack))
from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
queue = deque()

for i in range(n):
    com = input().split()

    if com[0] == "push_front":
        queue.appendleft(int(com[1]))

    elif com[0] == "push_back":
        queue.append(int(com[1]))

    elif com[0] == "pop_front":
        print(queue.popleft() if queue else -1)

    elif com[0] == "pop_back":
        print(queue.pop() if queue else -1)

    elif com[0] == "size":
        print(len(queue))

    elif com[0] == "empty":
        print(0 if queue else 1)

    elif com[0] == "front":
        print(queue[0] if queue else -1)

    elif com[0] == "back":
        print(queue[-1] if queue else -1)

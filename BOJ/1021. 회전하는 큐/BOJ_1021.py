from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
queue = deque(i for i in range(1, n + 1))
cnt = 0

for i in numbers:
    while True:
        if queue[0] == i:
            queue.popleft()
            break

        else:
            # 왼쪽으로 움직일지, 오른쪽으로 움직일지
            if len(queue) / 2 > queue.index(i):
                while queue[0] != i:
                    queue.append(queue.popleft())
                    cnt += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    cnt += 1

print(cnt)

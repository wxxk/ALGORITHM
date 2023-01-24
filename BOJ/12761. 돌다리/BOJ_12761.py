import sys
from collections import deque

# sys.stdin = open("input.txt")
input = sys.stdin.readline

# input
a, b, n, m = map(int, input().split())
matrix = [0] * (100001)

# 움직이는 거리
move = [-1, 1, a, -a, b, -b, a, b]

# 탐색
queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()

    # 종료
    if x == m:
        print(matrix[m])
        break

    for i in range(8):
        if i < 6:
            nx = x + move[i]
            if 0 <= nx < 100001 and matrix[nx] == 0:
                matrix[nx] = matrix[x] + 1
                queue.append(nx)
        else:
            nx = x * move[i]
            if 0 <= nx < 100001 and matrix[nx] == 0:
                matrix[nx] = matrix[x] + 1
                queue.append(nx)

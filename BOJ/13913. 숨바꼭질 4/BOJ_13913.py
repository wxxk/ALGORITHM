from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001
queue = deque()
queue.append((n, [n], 0))
visited[n] = 1

if n > k:
    print(n - k)
    for i in range(n, k - 1, -1):
        print(i, end=" ")
else:

    while queue:
        x, result, cnt = queue.popleft()

        if x == k:
            print(cnt)
            print(*result)
            break

        for i in (x * 2, x - 1, x + 1):
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = True
                queue.append((i, result + [i], cnt + 1))

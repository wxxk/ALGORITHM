import sys
from collections import deque

input = sys.stdin.readline
sys.stdin = open("input.txt")

S = int(input())
visited = [[-1] * (S + 1) for _ in range(S + 1)]
visited[1][0] = 1

queue = deque()
queue.append((1, 0, 0))

while queue:
    now, clip, time = queue.popleft()

    if now == S:
        print(time)
        # print(visited[now][now])
        break

    # 1번 조건 : 복사
    if visited[now][now] == -1:
        visited[now][now] = visited[now][clip] + 1
        queue.append((now, now, time + 1))

    if 2 <= now + clip < S + 1 and visited[now + clip][clip] == -1:
        visited[now + clip][clip] = visited[now][clip] + 1
        queue.append((now + clip, clip, time + 1))

    if 2 <= now - 1 < S + 1 and visited[now - 1][clip] == -1:
        visited[now - 1][clip] = visited[now][clip] + 1
        queue.append((now - 1, clip, time + 1))

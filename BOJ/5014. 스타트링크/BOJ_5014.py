from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [-1] * (F + 1)

queue = deque()
queue.append(S)
visited[S] = 0

while queue:
    cur = queue.popleft()

    if cur == G:
        print(visited[cur])
        break

    for i in (U, -D):
        next = cur + i
        if 0 < next <= F and visited[next] == -1:
            visited[next] = visited[cur] + 1
            queue.append(next)

else:
    print("use the stairs")

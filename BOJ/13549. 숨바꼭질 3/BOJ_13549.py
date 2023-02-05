from heapq import heappush, heappop
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, k = map(int, input().split())

visited = [INF] * 100001
maps = []
heappush(maps, (0, n))
visited[n] = 0

while maps:
    dis, x = heappop(maps)

    if x == k:
        print(dis)
        break

    for i in (x - 1, x + 1, x * 2):
        if 0 <= i < 100001:
            if i == x * 2:
                # 순간이동은 0초 후 이동
                next_dis = dis
            else:
                # 앞뒤는 1초 후 이동
                next_dis = dis + 1

            if visited[i] > next_dis:
                visited[i] = next_dis
                heappush(maps, (next_dis, i))

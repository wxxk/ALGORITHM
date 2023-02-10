from heapq import heappush, heappop
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(x):
    visited = [INF] * (n+1)
    visited[x] = 0
    queue = []
    heappush(queue, (0, x))

    while queue:
        cost, node = heappop(queue)

        if cost > visited[node]:
            continue
        
        for sCost, sNode in maps[node]:
            next_cost = cost+sCost

            if visited[sNode] > next_cost:
                visited[sNode] = next_cost
                heappush(queue, (next_cost, sNode))

    return visited  

n, e = map(int, input().split())
maps = [[] for _ in range(n+1)]

for i in range(e):
    start, end, cost = map(int,input().split())
    maps[start].append((cost, end))
    maps[end].append((cost, start))

v1, v2 = map(int, input().split())

visit_0 = dijkstra(1)
visit_1 = dijkstra(v1)
visit_2 = dijkstra(v2)

result = min(visit_0[v1]+visit_1[v2]+visit_2[n], visit_0[v2]+visit_2[v1]+visit_1[n])

print(result if result < INF else -1)
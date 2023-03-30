import sys

n = 4
INF = sys.maxsize

# 자료 배열
matrix = [[0, 5, INF, 8], [7, 0, 9, INF], [2, INF, 0, 4], [INF, INF, 3, 0]]

# 결과 그래프
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        visited[i][j] = matrix[i][j]

# k = 거쳐가는 노드
for k in range(n):
    # i = 출발 노드
    for i in range(n):
        # j = 도착 노드
        for j in range(n):
            # 바로가는 노드와 거쳐가는 노드 비교
            if visited[i][k] + visited[k][j] < visited[i][j]:
                visited[i][j] = visited[i][k] + visited[k][j]

# 결과 출력
print(visited)

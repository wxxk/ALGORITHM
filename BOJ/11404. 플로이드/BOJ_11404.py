import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())

matrix = [[INF] * n for _ in range(n)]

# 자료 배열
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = min(c, matrix[a][b])


for k in range(n):  # 거쳐가는 노드
    for i in range(n):  # 출발 노드
        for j in range(n):  # 도착 노드
            # 바로가는 노드와 거쳐가는 노드 비교
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

for i in range(n):
    for j in range(n):
        # 자기자신 0 처리
        if i == j:
            matrix[i][j] = 0
        # 방문할 수 없는 곳 처리
        elif matrix[i][j] == INF:
            matrix[i][j] = 0
        # 출력
        print(matrix[i][j], end=" ")
    print()

import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
matrix = [[INF] * v for _ in range(v)]

for _ in range(e):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    matrix[a][b] = c

for k in range(v):
    for j in range(v):
        for i in range(v):
            if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                matrix[i][j] = matrix[i][k] + matrix[k][j]

"""
# 사이클은 출발지와 도착지가 같은 경우
print(matrix)
[[8, 1, 5], 
 [3, 3, 2], 
 [3, 1, 3]]

"""
answer = INF
for i in range(v):
    answer = min(answer, matrix[i][i])

if answer == INF:
    print(-1)
else:
    print(answer)

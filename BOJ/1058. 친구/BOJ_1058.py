import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
matrix = [list(map(str, input().strip())) for _ in range(n)]

visited = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if matrix[i][j] == "Y" or matrix[i][k] == "Y" and matrix[k][j] == "Y":
                visited[i][j] = 1

answer = 0
for i in visited:
    answer = max(answer, sum(i))

print(answer)

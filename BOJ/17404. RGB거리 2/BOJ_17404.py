import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

r, g, b = 0, 1, 2

n = int(input())
matrix = [[-1, -1, -1]]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

answer = INF

for color in [r, g, b]:
    dp = [[-1] * 3 for _ in range(n + 1)]

    dp[1] = [INF, INF, INF]
    dp[1][color] = matrix[1][color]

    for i in range(2, n + 1):
        dp[i][r] = min(dp[i - 1][g], dp[i - 1][b]) + matrix[i][r]
        dp[i][g] = min(dp[i - 1][r], dp[i - 1][b]) + matrix[i][g]
        dp[i][b] = min(dp[i - 1][r], dp[i - 1][g]) + matrix[i][b]
    dp[n][color] = INF
    answer = min(answer, min(dp[n]))

print(answer)

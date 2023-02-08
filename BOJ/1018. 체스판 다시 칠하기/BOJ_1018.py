import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
result = []

for i in range(n - 7):
    for j in range(m - 7):
        fw = 0
        fb = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                # 행과 열이 짝수인 경우 같은 색
                if (k + l) % 2 == 0:
                    if matrix[k][l] != "W":
                        fw += 1
                    if matrix[k][l] != "B":
                        fb += 1
                # 행과 열이 홀수인 경우도 같은색
                else:
                    if matrix[k][l] != "B":
                        fw += 1
                    if matrix[k][l] != "W":
                        fb += 1
        result.append(fw)
        result.append(fb)

print(min(result))

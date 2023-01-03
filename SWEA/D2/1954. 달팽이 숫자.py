import sys

sys.stdin = open("input.txt")

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    x = 0
    y = -1
    val = 1
    move = 1
    matrix = [[0] * n for _ in range(n)]

    while n > 0:
        for j in range(n):
            y += move
            matrix[x][y] = val
            val += 1

        n -= 1
        if n == 0:
            break

        for k in range(n):
            x += move
            matrix[x][y] = val
            val += 1

        move *= -1

    print(f"#{i}")
    for result in matrix:
        print(*result)

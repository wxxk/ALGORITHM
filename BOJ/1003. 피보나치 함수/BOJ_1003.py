import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline


def fibonacci(n):
    # 0이랑 1이 나오는 갯수도 피보나치
    z = [1, 0, 1]
    o = [0, 1, 1]

    if n >= 3:
        for i in range(3, n + 1):
            z.append(z[i - 2] + z[i - 1])
            o.append(o[i - 2] + o[i - 1])

    print(z[n], o[n])


t = int(input())

for _ in range(t):
    n = int(input())
    fibonacci(n)

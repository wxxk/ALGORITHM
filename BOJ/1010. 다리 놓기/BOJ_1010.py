import sys
import math

# sys.stdin = open("input.txt")
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ans = math.factorial(m) // (math.factorial(m - n) * math.factorial(n))
    print(ans)

import sys

# sys.stdin = open('input.txt')
input = sys.stdin.readline
from math import factorial

n, k = map(int, input().split())

result = factorial(n) / (factorial(n - k) * factorial(k))

print(int(result))

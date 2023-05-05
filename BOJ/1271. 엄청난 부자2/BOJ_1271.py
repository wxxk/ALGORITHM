import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())

ans1 = n // m
ans2 = n % m
print(ans1)
print(ans2)
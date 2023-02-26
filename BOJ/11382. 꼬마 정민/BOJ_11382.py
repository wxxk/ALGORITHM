import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(a+b+c)
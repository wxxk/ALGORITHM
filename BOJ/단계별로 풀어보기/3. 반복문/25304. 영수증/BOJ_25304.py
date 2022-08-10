import sys
sys.stdin = open ('25304.txt')

X = int(input())
N = int(input())
sum = 0
for i in range(N):
    a, b = map(int, input().split())
    sum += (a*b)

if X == sum:
    print('Yes')
else:
    print('No')
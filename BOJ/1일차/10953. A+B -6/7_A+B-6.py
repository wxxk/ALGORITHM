import sys

sys.stdin = open('6_A+B-3.txt')

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split(','))
    print(A+B)
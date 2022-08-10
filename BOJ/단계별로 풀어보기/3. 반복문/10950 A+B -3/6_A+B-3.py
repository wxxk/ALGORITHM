import sys

sys.stdin = open("5_A+B-2.txt")

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())
    print(A + B)
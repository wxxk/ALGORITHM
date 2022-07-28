import sys
sys.stdin = open ('2711.txt')

T = int(input())

for i in range(1, T+1):
    A, B = input().split()
    A = int(A)
    print(B[:A-1], B[A:], sep='')

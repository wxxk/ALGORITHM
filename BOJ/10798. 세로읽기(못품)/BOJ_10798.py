import sys
sys.stdin = open('10798.txt')

A = list(input())
B = list(input())
C = list(input())
D = list(input())
E = list(input())

for i in range(len(max(A, B, C, D, E))):
    print(A[i], end='')
    print(B[i], end='')
    print(C[i], end='')
    print(D[i], end='')
    print(E[i], end='')
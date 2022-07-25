import sys
sys.stdin = open('9_별찍기-2.txt')

N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '*'*i)
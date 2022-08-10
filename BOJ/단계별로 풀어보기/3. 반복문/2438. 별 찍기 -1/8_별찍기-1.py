import sys
sys.stdin = open('8_별찍기-1.txt')

N = int(input())

for i in range(1, N+1):
    print('*'*i)
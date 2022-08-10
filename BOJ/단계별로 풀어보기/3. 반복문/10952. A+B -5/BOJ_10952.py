import sys
sys.stdin = open ('BOJ_10952.txt')

while True:
    A, B = map(int, input().split())
    if A != 0 and B !=0:
        print(A + B)
    else:
        break
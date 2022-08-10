import sys
sys.stdin = open('11_두수비교.txt')

T = int(input())

for i in range(1, T+1):
    A, B = map(int, input().split())

    if A > B:
        print('>')
    elif A < B :
        print('<')
    else:
        print('==')
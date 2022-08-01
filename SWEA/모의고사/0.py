import sys
sys.stdin = open('0.txt')
T = int(input())

for i in range(1, T+1):
    num = int(input())
    score = list(map(int, input().split()))
    A = [0] * 101

    for i in score:
        A[i] += 1

    if A.count(max(A)) >= 2:
        A[A.index(max(A))] = 0
        print(f'#{num} {A.index(max(A))}')
    else:
        print(f'#{num} {A.index(max(A))}')

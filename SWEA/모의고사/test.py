import sys
sys.stdin = open('test.txt')

score = list(map(int, input().split()))
A = [0] * 101
score_set = list(set(score))
most = []
for i in score:
    A[i] += 1

if A.count(max(A)) >= 2:
    A[A.index(max(A))] = 0
    print(A.index(max(A)))
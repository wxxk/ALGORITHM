import sys
sys.stdin = open ('2511.txt')

score_A = 0
score_B = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))
win = 'D'

for i in range(10):
    if A[i] > B[i]:
        score_A += 3
        win = 'A'
    elif B[i] > A[i]:
        score_B += 3
        win = 'B'
    else:
        score_A += 1
        score_B += 1

if score_A > score_B:
    print(score_A, score_B)
    print('A')
    
elif score_B > score_A:
    print(score_A, score_B)
    print('B')
   
else:
    if win == 'A':
        print(score_A, score_B)
        print('A')
    elif win == 'B':
        print(score_A, score_B)
        print('B')
    elif win == 'D':
        print(score_A, score_B)
        print('D')
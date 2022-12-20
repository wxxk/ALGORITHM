import sys
sys.stdin = open('BOJ_2753.txt')

T = int(input())

for i in range(1, T+1):
    years = int(input())
# 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다
    if years%4 == 0 and years%100 != 0 :
        print(1)
    elif years%4 == 0 and years%400 == 0:
        print(1)
    else:
        print(0)
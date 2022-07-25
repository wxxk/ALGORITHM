# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1, T+1):
    sum = 0 # 0의 개수를 더할 변수
    cnt = 0 # dusthrehls 0의 개수
    result = input()
    for i in result:
        if i == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
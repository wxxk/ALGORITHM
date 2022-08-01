import sys
sys.stdin = open('10816.txt')

N = int(input().rstrip())
card=list(map(int,input().split()))
M = int(input().rstrip())
finds =list(map(int,input().split()))

dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for j in finds:
    if j in dic:
        print(dic[j], end=' ')
    else:
        print(0, end=' ')
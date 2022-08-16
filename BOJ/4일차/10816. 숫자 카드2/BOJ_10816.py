import sys
sys.stdin = open('10816.txt')

N = int(input().rstrip())
card=list(map(int,input().split()))
M = int(input().rstrip())
finds =list(map(int,input().split()))

dic = {}

for i in card: # 6 3 2 10 10 10 -10 -10 7 3 하나씩 돈다
    if i in dic:
        dic[i] += 1 # dic에 있으면 +1
    else:
        dic[i] = 1 # dic에 없으면 1

for j in finds: # 10 9 -5 2 3 4 5 -10
    if j in dic:
        print(dic[j], end=' ')
    else:
        print(0, end=' ')
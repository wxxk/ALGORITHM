import sys

input = sys.stdin.readline

k, l = map(int, input().split())
dic = {}

for i in range(l):
    dic[input().strip()] = i

res = sorted(dic.items(), key=lambda x: x[1])

if k > len(res):
    k = len(res)

for i in range(k):
    print(res[i][0])

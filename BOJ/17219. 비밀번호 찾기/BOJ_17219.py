import sys

sys.stdin = open("input.txt")

dic = {}
n, m = map(int, input().split())

for _ in range(n):
    a, p = map(str, input().split(" "))
    dic[a] = p


for i in range(m):
    answer = input()
    print(dic[answer])

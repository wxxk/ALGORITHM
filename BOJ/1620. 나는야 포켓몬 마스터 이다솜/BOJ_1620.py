import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())
dict_1 = {}

for i in range(1, n+1):
    word = input()
    dict_1[str(i)] = word
    dict_1[word] = i

for i in range(m):
    print(dict_1[input()])

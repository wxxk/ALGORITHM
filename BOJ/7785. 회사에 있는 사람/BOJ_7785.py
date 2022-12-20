import sys
sys.stdin = open('7785.txt')

N = int(sys.stdin.readline())
dict = {}

for _ in range(N):
    a, b = map(str, sys.stdin.readline().split())

    if b == 'enter':
        dict[a] = 1
    else:
        del dict[a]

for i in sorted(dict, reverse=True):
    print(i)
import sys
sys.stdin = open('10798.txt')

words = [[0]*15 for i in range(5)]

for i in range(5):
    d = list(input())
    d_len = len(d)
    for j in range(d_len):
        words[i][j] = d[j]

for i in range(15):
    for j in range(5):
        if words[j][i] !=0:
            print(words[j][i], end='')
        else:
            continue
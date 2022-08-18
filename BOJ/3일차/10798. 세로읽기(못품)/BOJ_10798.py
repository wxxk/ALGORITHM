import sys
sys.stdin = open('10798.txt')

words = [input() for _ in range(5)]

for i in range(max(len(w) for w in words)):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
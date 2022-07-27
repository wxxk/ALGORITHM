import sys
sys.stdin = open('2789.txt')
T = int(input())

for i in range(1, T+1):
    word = input()
    for i in "CAMBRIDGE":
        word = word.replace(i, '')
    print(word)
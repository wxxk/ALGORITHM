import sys
sys.stdin = open ('1316.txt')

T = int(input())

for i in range(1, T+1):
    word = list(map(str, input()))
    print(word)
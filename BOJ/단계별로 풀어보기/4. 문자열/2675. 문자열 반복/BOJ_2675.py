import sys
sys.stdin = open('2675.txt')

T = int(input())

for tc in range(T):
    num, word = input().split()
    for i in word:
        print(i*int(num), end='') 
    print()
import sys
sys.stdin = open ('BOJ_14681.txt')
T = int(input())

for i in range(1, T+1):
    x = int(input())
    y = int(input())

    if x > 0 and y > 0:
        print(1)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x > 0 and y < 0:
        print(4)
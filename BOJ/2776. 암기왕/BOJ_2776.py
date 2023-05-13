import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    num_1 = set(map(int, input().split()))
    m = int(input())
    num_2 = list(map(int, input().split()))

    for i in num_2:
        if i in num_1:
            print(1)
        else:
            print(0)

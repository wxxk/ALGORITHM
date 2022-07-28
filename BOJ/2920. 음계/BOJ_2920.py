import sys
sys.stdin = open("2920.txt")

T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))

    if numbers == sorted(numbers):
        print('ascending')
    elif numbers == sorted(numbers, reverse=True):
        print('descending')
    else:
        print('mixed')
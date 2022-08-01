import sys
sys.stdin = open('4.txt')
T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    odd_number = 0
    even_number= 0 
    N = 0

    for j in range(0, len(numbers), 2):
        odd_number += numbers[j] * 2
    for k in range(1, len(numbers), 2):
        even_number += numbers[k]

    sum = odd_number + even_number
    if sum%10 == 0:
        print(f'#{i} {sum%10}')
    else:
        while sum%10 != 0:
            sum += 1
            N += 1
        print(f'#{i} {N}')
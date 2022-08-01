import sys
sys.stdin = open('3.txt')

T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    D = 0

    for j in numbers:
        if numbers.count(j) == 3:
            D = numbers[0]
        else:
            if numbers.count(max(numbers)) == 1:
                D = max(numbers)
            else:
                D = min(numbers)
    print(f'#{i} {D}')

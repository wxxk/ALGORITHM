import sys
sys.stdin = open('4344.txt')

T = int(input())

for tc in range(T):
    numbers = list(map(int, input().split()))
    N = numbers.pop(0)
    avg = (sum(numbers)/N)
    cnt = 0
    for i in range(len(numbers)):
        if numbers[i] > avg:
            cnt += 1

    rate = (cnt/N) * 100
    print(f'{rate:.3f}%')
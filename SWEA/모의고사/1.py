import sys
sys.stdin = open ('1.txt')
T = int(input())
for i in range(1, T+1):
    N = int(input())
    income = list(map(int, input().split()))
    sum_list = sum(income)
    avg = (sum_list/N)
    cnt = 0

    for j in range(len(income)):
        if income[j] <= avg:
            cnt += 1
    print(f'#{i} {cnt}')

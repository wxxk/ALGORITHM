import sys
sys.stdin = open('1065.txt')

N = int(input())
cnt = 0
for i in range(1, N+1):
    if len(str(i)) < 3:
        cnt += 1
    else:
        numbers = list(map(int, str(i)))
        if numbers[0] - numbers[1] == numbers[1] - numbers[2]:
            cnt += 1
        # print(numbers)
print(cnt)
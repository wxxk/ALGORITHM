import sys
sys.stdin = open('1110.txt')

N = int(input())

num = N
cnt = 0

while True:
    sum_num = (num // 10) + (num % 10) # 8
    new_num = (num % 10 * 10) + (sum_num % 10)
    cnt += 1
    if new_num == N:
        break
    num = new_num
print(cnt)
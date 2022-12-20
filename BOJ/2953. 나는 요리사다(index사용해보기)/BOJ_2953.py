import sys
sys.stdin = open ('2953.txt')
sum_score = 0
line = 0

for i in range(1, 6):
    score = sum(map(int, input().split()))
    if score > sum_score:
        sum_score = score
        line = i

print('{} {}'. format(line, sum_score))
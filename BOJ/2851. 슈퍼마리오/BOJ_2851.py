import sys
sys.stdin = open('2851.txt')

T = 10
sum = 0
sum_2 = 0

for i in range(T):
    number = int(input())
    sum += number
    if sum >= 100:
        break
    sum_2 = sum

if (sum-100) > (100 -sum_2):
    print(sum_2)
elif (100 - (sum%100)) < (100 -sum_2):
    print(sum)
else:
    print(max(sum, sum_2))
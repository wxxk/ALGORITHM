import sys
sys.stdin = open('1546.txt')

N = int(input())
numbers = list(map(int, input().split()))
max_num = 0
max_num = max(numbers)

for i in range(N):
    numbers[i] = (numbers[i]/max_num)*100

print(sum(numbers)/N)
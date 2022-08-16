import sys
sys.stdin = open ('11720.txt')\

num = int(input())
numbers = str(input())
total = 0

for i in range(num):
    total += int(numbers[i])

print(total)
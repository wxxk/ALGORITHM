import sys
sys.stdin = open('3052.txt')

N = 10
numbers = []
remain = []

for _ in range(N):
    numbers.append(int(input())) 

for i in range(len(numbers)):
    remain.append(numbers[i]%42)

print(len(set(remain)))
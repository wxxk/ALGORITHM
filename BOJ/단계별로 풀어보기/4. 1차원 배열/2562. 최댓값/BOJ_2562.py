import sys
sys.stdin = open('2562.txt')

N = 9
numbers = [0]

for _ in range(N):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers)))
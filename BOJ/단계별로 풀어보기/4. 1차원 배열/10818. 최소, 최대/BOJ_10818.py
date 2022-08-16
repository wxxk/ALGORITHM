import sys
sys.stdin = open('10818.txt')

N = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))
import sys
sys.stdin = open('2908.txt')

num1, num2 = map(str, input().split())

num1 = int(str(num1)[::-1])
num2 = int(str(num2)[::-1])

print(max(num1, num2))
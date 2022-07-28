import sys
sys.stdin = open ('17249.txt')

left, right = input().split('(^0^)')

print(left.count('@'), right.count('@'), end = ' ')
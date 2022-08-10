import sys
sys.stdin = open('2525.txt')
H, M = map(int, input().split())
min = int(input())

H += min // 60
M += min % 60

if M >= 60:
    H += 1
    M -= 60
if H >= 24:
    H -=24

print(H, M)
import sys
sys.stdin = open ('2609.txt')

A, B = map(int, input().split())
n, m = max(A, B), min(A, B)

# 유클리드 호제법
# (24, 18, 6) a, b, 나머지
# (18, 6, 0)
# 나머지가 0이되면 최대 공약수 = 6
# (A*B) / 최대 공약수 = 최소 공배수

while m > 0:
    n, m = m, n%m

print(n)
print((A*B)//n)
import sys
sys.stdin = open ('BOJ_2480.txt')

T = int(input())

for i in range(1, T+1):
    A, B, C = map(int, input().split())
    sum = 0
    if A == B == C:
        sum = 10000 + (A*1000)
    elif A == B and A != C:
        sum = 1000 + (A*100)
    elif A != B and A == C:
        sum = 1000 + (A*100)
    elif A != B and B == C:
        sum = 1000 + (A*100)
    else:
        if A > B and A > C:
            sum = A * 100
        elif B > A and B > C:
            sum = B * 100
        elif C > A and C > A:
            sum = C * 100
    print(sum)


# 간단한 풀이
# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))
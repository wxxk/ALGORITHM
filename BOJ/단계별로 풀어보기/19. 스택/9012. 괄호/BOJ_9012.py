import sys
sys.stdin = open('9012.txt')

N = int(input())

for _ in range(1, N+1):
    PS = input()
    stack = []
    for i in PS:
        if i == '(':
            stack.append(i)
        else:
            if len(stack)>=1:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack)==0:
            print('YES')
        else:
            print('NO')
import sys
sys.stdin = open('1874.txt')

n = int(input())
num = 0
count = 1
stack = []
answer = []
flag = 0

for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        answer.append('+')
        count+=1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)

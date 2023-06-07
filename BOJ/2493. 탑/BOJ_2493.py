import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

stack = []  # 최대값을 저장할 스택
answer = []  # 수신 탑 인덱스 저장

for i in range(n):
    while stack:
        if stack[-1][1] > num[i]:
            answer.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if not stack:
        answer.append(0)
    stack.append([i, num[i]])

print(*answer)

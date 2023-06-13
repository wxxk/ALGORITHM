import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
number = list(map(int, input().split()))
stack = []
res = [-1] * n

for i in range(n):
    while stack and number[stack[-1]] < number[i]:
        res[stack.pop()] = number[i]
    stack.append(i)

print(*res)

"""
1. 오큰수가 없으면 -1을 출력해야하기때문에 -1로 초기화
2. 스택에 인덱스를 저장 -> 다음 큰 수의 위치를 찾기 위해

"""

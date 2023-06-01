import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input())
num = sorted(list(map(int, input().split())))

x = 0
y = n - 1

result = abs(num[x] + num[y])
result_index = [num[x], num[y]]

while x < y:
    # 절대값으로 계산해서 result보다 작으면 0에 가까운 수
    if abs(num[x] + num[y]) < result:
        result = abs(num[x] + num[y])
        result_index = [num[x], num[y]]
        if result == 0:
            break

    if num[x] + num[y] < 0:
        x += 1
    else:
        y -= 1

print(*result_index)

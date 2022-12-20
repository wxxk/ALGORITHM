import sys

sys.stdin = open("input.txt")

n = int(input())
bubble = []

for i in range(n):
    bubble.append(int(input()))

for i in range(n - 1):  # 정렬된 영역을 지정해주기위한 범위
    # i = 0 1 2 3
    for j in range(n - 1 - i):  # 정렬된 영역은 제외하기 위해 -i
        # j = 0 1 2 3 4
        # j = 0 1 2 3
        # j = 0 1 2
        # j = 0 1
        # j = 0

        if bubble[j] > bubble[j + 1]:  # 옆에 있는 숫자와 비교
            # 조건에 맞는 다면 swap
            # temp = bubble[j]
            # bubble[j] = bubble[j + 1]
            # bubble[j + 1] = temp

            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]

# print(bubble)
for i in range(len(bubble)):
    print(bubble[i])

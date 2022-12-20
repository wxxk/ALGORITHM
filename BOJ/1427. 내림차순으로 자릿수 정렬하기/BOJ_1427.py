import sys

sys.stdin = open("input.txt")

num = list(map(int, input()))

for i in range(len(num)):
    max = i
    for j in range(i + 1, len(num)):
        if num[j] > num[max]:
            max = j

    if num[i] < num[max]:
        num[i], num[max] = num[max], num[i]

for i in num:
    print(i, end="")

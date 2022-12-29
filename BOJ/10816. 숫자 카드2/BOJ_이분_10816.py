import sys

sys.stdin = open("10816.txt")

m = int(input())
a = sorted(list(map(int, input().split())))

n = int(input())
num = list(map(int, input().split()))

result = [0] * 8

for i in range(len(num)):
    start = 0
    end = len(a) - 1

    while end >= start:
        mid = (start + end) // 2

        if a[mid] == num[i]:
            result[i] += 1
            break

        elif a[mid] > num[i]:
            end = mid - 1

        else:
            start = mid + 1

print(result)

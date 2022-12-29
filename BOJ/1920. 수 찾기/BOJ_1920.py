import sys

sys.stdin = open("input.txt")

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
num = list(map(int, input().split()))

start = 0
end = len(a) - 1

for i in range(m):
    start = 0
    end = len(a) - 1
    ex = False

    while start <= end:
        mid = (start + end) // 2

        if a[mid] == num[i]:
            print(1)
            ex = True
            break

        elif a[mid] > num[i]:
            end = mid - 1

        elif a[mid] < num[i]:
            start = mid + 1

    if not ex:
        print(0)

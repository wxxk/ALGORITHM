import sys

input = sys.stdin.readline

a, b = map(int, input().split())
num_a = sorted(list(map(int, input().split())))
num_b = sorted(list(map(int, input().split())))
res = []

for i in range(a):
    start = 0
    end = b - 1

    while start <= end:
        mid = (start + end) // 2

        if num_b[mid] == num_a[i]:
            break

        if num_b[mid] > num_a[i]:
            end = mid - 1

        else:
            start = mid + 1

    else:
        res.append(num_a[i])

print(len(res))
print(*res)

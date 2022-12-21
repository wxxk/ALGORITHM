import sys

sys.stdin = open("input.txt")

# N, K = map(int, input().split())
# num = sorted(list(map(int, input().split())))

# print(num[K - 1])
def quick(data, start, end):
    if start >= end:
        return

    key = start
    i = start + 1
    j = end

    while i <= j:
        while data[i] <= data[key]:
            i += 1
        while data[j] >= data[key]:
            j -= 1

        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[i], data[j] = data[j], data[i]

    quick(data, start, j - 1)
    quick(data, j + 1, end)


N, K = map(int, input().split())
data = list(map(int, input().split()))

quick(data, 0, N - 1)

print(data)
print(data[K - 1])

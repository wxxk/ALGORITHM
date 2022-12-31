import sys

sys.stdin = open("input.txt")

k, n = map(int, input().split())
arr = []

for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(k):
        cnt += arr[i] // mid

    if cnt >= n:
        start = mid + 1

    else:
        end = mid - 1

print(end)

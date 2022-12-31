import sys

sys.stdin = open("10816.txt")

m = int(input())
cards = sorted(list(map(int, input().split())))
n = int(input())
nums = list(map(int, input().split()))
count = {}


def binarySearch(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return count.get(target)

    elif arr[mid] > target:
        return binarySearch(arr, target, start, mid - 1)

    else:
        return binarySearch(arr, target, mid + 1, end)


for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for target in nums:
    print(binarySearch(cards, target, 0, len(cards) - 1), end=" ")

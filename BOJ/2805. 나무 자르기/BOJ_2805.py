import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

# 이분탐색
while end >= start:
    mid = (start + end) // 2
    cnt = 0

    for i in range(n):
        if tree[i] - mid >= 0:
            cnt += tree[i] - mid  # 마이너스일 경우 cnt에서 빠지기 때문에

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

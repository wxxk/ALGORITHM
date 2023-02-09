import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

nums.sort()

start, end = 0, max(nums)

# 이분 탐색
while end >= start:
    # 상한액 설정
    mid = (start + end) // 2
    cnt = 0

    for i in nums:
        # 요청한 금액이 상한액 이상이라면
        if i >= mid:
            # 상한액 더하기
            cnt += mid
        # 상한액 미만이라면
        else:
            # 요청한 금액 더하기
            cnt += i

    # 예산 총액이 총 예산 이하라면
    if cnt <= m:
        start = mid + 1
    # 예산 총액이 총 예산을 초과한다면
    else:
        end = mid - 1

print(end)

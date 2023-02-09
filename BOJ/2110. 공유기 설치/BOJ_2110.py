import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, c = map(int, input().split())
nums = [int(input().strip()) for _ in range(n)]

# 공유기 좌표들 오름차순으로 정렬
nums.sort()
# print(nums)

# 공유기를 설치할 수 있는 최소 간격과 최대 간격을 구한 뒤,
# 공유기를 가장 공평하게 설치할 수 있는 mid 간격을 구한다.
start = 1  # 최소 거리
end = nums[-1] - nums[0]  # 최대 거리

while start <= end:
    mid = (start + end) // 2
    count = 1

    # 첫 번째 집에 공유기를 설치한뒤,
    # 첫 번째 집에서 나머지 집들 간의 간격을 확인하며, mid 이상으로 떨어져 있는 집을 탐색
    ins = nums[0]

    for i in nums:
        if i >= ins + mid:

            # 첫 번째 집으로부터 mid 이상 떨어진 집을 찾은 경우,
            # 해당 집에 공유기를 설치한 뒤, 해당 집 기준으로 다시 mid 만큼 떨어져 있는 집을 탐색
            count += 1
            ins = i

    # 모든 집을 탐색했다면, 공유기 설치 간격을 이분법을 사용해 갱신
    # 1. 현재까지 설치한 공유기의 개수가 아직 C개 이하라면, 기존 간격이 너무크다는 의미이므로, 기존 간격보다 더 작은 간격으로 갱신
    # 2. 현재까지 설치한 공유기의 개수가 C개 이상이라면, 기존 간격이 너무 작다는 의미이므로, 기존 간격보다 더 큰 간격으로 갱신
    if count >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)

import sys

# sys.stdin = open("input.txt")

n = int(input())
t = []
p = []
dp = [0 for _ in range(n + 1)]

for i in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n - 1, -1, -1):
    # 상담에 필요한 일 수가 퇴사일을 넘어가는 경우
    if t[i] + i > n:
        # 상담이 불가능하기 때문에 다음날 dp값을 가져옴
        dp[i] = dp[i + 1]

    # 퇴사일을 넘어가지 않을 경우
    else:
        # 오늘 상담을 하지 않을 경우 = dp[i+1] 지난 상담 보수
        # 오늘 상담을 할 경우 = dp[t[i]+1]+p[i] (dp[오늘 날짜 + 오늘 시작할 상담에 필요한 일 수]+상담 보수)

        dp[i] = max(dp[i + 1], dp[t[i] + i] + p[i])

print(dp[0])

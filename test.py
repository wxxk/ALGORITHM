def solution_1(n, money, events):
    """
    500, 100, ["10 x2", "5 +100", "20 +200", "100 x3", "80 x2"]
    2400
    """

    answer = 0
    cost = [0]
    count = [0]
    dp = [[n for _ in range(money + 1)] for _ in range(len(events) + 1)]

    for i in events:
        a, b = i.split(" ")
        cost.append(int(a))
        count.append(b)

    for i in range(1, len(events) + 1):
        for j in range(1, money + 1):
            w = cost[i]
            v = count[i]

            if w > j:
                dp[i][j] = dp[i - 1][j]
            else:
                if v[0] == "x":
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - w] * int(v[1:])))

                elif v[0] == "+":
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + int(v[1:]))

    for i in dp:
        print(i)

    answer = dp[-1][-1]

    return answer


def solution_2(image):
    answer = []
    for i in range(len(image)):
        # 정방향
        answer.append(image[i])
        for j in range(len(image) - 1, -1, -1):
            # 가로
            answer[i].append(image[i][j])

    for i in range(len(answer) - 1, -1, -1):
        answer.append(answer[i])

    return answer

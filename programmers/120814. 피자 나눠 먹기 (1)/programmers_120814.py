n = 1


def solution(n):
    answer = 0

    # 피자 한판을 시켰을 때 피자가 모자를 경우
    if n % 7 != 0:
        answer = (n // 7) + 1

    # 피자 한판을 시켰을 때 다 먹을 수 있는 경우
    else:
        answer = n // 7

    return answer


print(solution(n))
print(7 % 7)

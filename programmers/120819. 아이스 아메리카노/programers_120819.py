money = 5500


def solution(money):
    answer = []
    ice = money // 5500
    remain = money % 5500
    answer = [ice, remain]
    return answer


print(solution(money))

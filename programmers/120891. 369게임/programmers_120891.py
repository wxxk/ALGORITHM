def solution(order):
    answer = 0
    order = str(order)

    for i in range(3, 10, 3):
        answer += order.count(str(i))
    return answer


order = 29423
print(solution(order))

from itertools import combinations


def solution(nums):
    answer = 0
    com = list(combinations(nums, 3))

    for i in com:
        if check(i[0], i[1], i[2]):
            answer += 1
    return answer


def check(a, b, c):
    total = a + b + c
    for i in range(2, total):
        if total % i == 0:
            return False
    return True


nums = [1, 2, 3, 4]

print(solution(nums))

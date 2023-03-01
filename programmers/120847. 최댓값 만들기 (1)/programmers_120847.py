from itertools import combinations

numbers = [0, 31, 24, 10, 1, 9]


# def solution(numbers):
#     answer = 0
#     temp = 0

#     for i, j in combinations(numbers, 2):

#         if (i * j) > temp:
#             temp = i * j
#     answer = temp
#     return answer


def solution(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


print(solution(numbers))

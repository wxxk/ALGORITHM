import math


def solution_1(balls, share):
    answer = (math.factorial(balls)) // (
        math.factorial((balls - share)) * math.factorial(share)
    )
    return answer


def solution_2(balls, share):
    answer = math.comb(balls, share)
    return answer


def solution_3(balls, share):
    answer = 0
    n = 1
    n_m = 1
    m = 1
    for i in range(1, balls + 1):
        n *= i

    for i in range(1, balls - share + 1):
        n_m *= i

    for i in range(1, share + 1):
        m *= i

    answer = n // (n_m * m)
    return answer


balls = 5
share = 3

print(solution_1(balls, share))
print(solution_2(balls, share))
print(solution_3(balls, share))

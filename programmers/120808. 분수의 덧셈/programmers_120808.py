def solution(denom1, numer1, denom2, numer2):
    denom = denom1 * denom2
    numer = (numer1 * denom2) + (numer2 * denom1)

    n, m = max(denom, numer), min(denom, numer)

    while m > 0:
        n, m = m, n % m

    answer = [numer // n, denom // n]
    return answer


numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

print(solution(denom1, numer1, denom2, numer2))

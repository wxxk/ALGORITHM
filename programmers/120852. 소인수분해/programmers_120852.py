def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            if d in answer:
                n = n / d
                continue
            else:
                answer.append(d)
                n = n / d
        else:
            d = d + 1
    return answer


n = 12
print(solution(n))

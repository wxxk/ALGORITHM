def solution(array, n):
    answer = 0
    min = 0
    array.sort()
    for i in array:
        if n - i == 0:
            return i

        if min > abs(n - i) or min == 0:
            min = abs(n - i)
            answer = i
    return answer


array = [10, 11, 12]
n = 13

print(solution(array, n))

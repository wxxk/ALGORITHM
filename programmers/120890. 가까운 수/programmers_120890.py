def solution(array, n):
    answer = 0
    min = 0

    array.sort()  # 가까운 수가 여러 개일 경우 더 작은 수를 return해야 하기 때문에
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

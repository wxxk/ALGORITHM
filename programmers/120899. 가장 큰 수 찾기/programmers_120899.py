def solution(array):
    answer = []
    max = 0
    for i in array:
        if i > max:
            max = i

    answer.append(max)
    answer.append(array.index(max))
    return answer


array = [9, 10, 11, 8]

print(solution(array))

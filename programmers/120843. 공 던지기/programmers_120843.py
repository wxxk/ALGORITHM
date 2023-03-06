def solution(numbers, k):
    answer = 0
    index = 0

    for i in range(1, k):
        index += 2
        index = index % len(numbers)

    answer = numbers[index]
    return answer


numbers = [1, 2, 3, 4, 5, 6]
k = 5

print(solution(numbers, k))

# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    for i in range(0, len(numbers)): # range(0, 5)
        for j in range(i+1, len(numbers)): # range(1, 5)
            result = numbers[j] + numbers[i] 
            answer.append(result)
    # same = set(answer)
    # answer = list(same)
    # answer.sort()
    return sorted(list(set(answer)))

print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
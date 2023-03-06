def solution(num_list, n):
    answer = []
    temp = []
    cnt = 0

    for i in num_list:
        temp.append(i)
        cnt += 1
        if cnt == n:
            answer.append(temp)
            temp = []
            cnt = 0

    return answer


num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
n = 3

print(solution(num_list, n))

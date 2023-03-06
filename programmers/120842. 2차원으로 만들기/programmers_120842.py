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


num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2

print(solution(num_list, n))

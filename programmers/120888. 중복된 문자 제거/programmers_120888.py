def solution(my_string):
    answer = ""
    for i in my_string:
        if i not in answer:
            answer += i
        else:
            continue
    return answer


my_string = "people"

print(solution(my_string))

def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit():
            answer += int(i)

    return answer


my_string = "aAb1B2cC34oOp"

print(solution(my_string))

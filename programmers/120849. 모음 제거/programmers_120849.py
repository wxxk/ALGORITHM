def solution(my_string):
    answer = ""
    gather = ["a", "e", "i", "o", "u"]

    for i in my_string:
        if i in gather:
            continue
        else:
            answer += i
    return answer


my_string = "bus"
print(solution(my_string))

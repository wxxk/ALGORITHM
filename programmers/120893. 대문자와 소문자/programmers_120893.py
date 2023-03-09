def solution(my_string):
    answer = ""
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        elif i.islower():
            answer += i.upper()

    return answer


my_string = "abCdEfghIJ"

print(solution(my_string))

def solution(s):
    answer = 0
    stack = []
    for i in s.split():
        if i == "Z":
            stack.pop()
        else:
            stack.append(int(i))
    answer = sum(stack)
    return answer


s = "-1 -2 -3 Z"
print(solution(s))

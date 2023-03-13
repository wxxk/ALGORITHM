def solution_1(s):
    answer = ""
    s2 = set(s)
    for i in s2:
        if s.count(i) == 1:
            answer += i
    answer = "".join(sorted(answer))
    return answer


def solution(s):
    answer = ""
    cntDict = {}
    for i in s:
        cntDict[i] = cntDict.get(i, 0) + 1

    for k, v in sorted(cntDict.items()):
        if v == 1:
            answer += k
    return answer


s = "abdc"

print(solution(s))

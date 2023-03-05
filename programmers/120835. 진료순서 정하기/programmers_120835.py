# 매개변수로 받은 배열을 복사한다.
# 복사한 배열을 내림차순으로 정렬한다.
# 복사된 배열과 원본을 비교해서 어디위치에 있는지 찾는다.
# 찾은 위치 +1 해서 리턴한다.


def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)

    for i in emergency:
        answer.append(temp.index(i) + 1)
    return answer


emergency = [3, 76, 24]
print(solution(emergency))

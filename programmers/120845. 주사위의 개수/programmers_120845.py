# 가로, 세로, 높이 별로 주사위 모서리가 몇 개 들어가는지 확인
def solution(box, n):
    answer = 0
    x = box[0] // n
    y = box[1] // n
    z = box[2] // n

    answer = x * y * z

    return answer


box = [10, 8, 6]
n = 3

print(solution(box, n))

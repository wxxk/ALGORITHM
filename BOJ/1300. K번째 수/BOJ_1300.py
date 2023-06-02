import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline


def find_B_k(n, k):
    start = 1
    end = n * n

    while start <= end:
        mid = (start + end) // 2  # 중간점 계산
        count = 0  # 중간점보다 작거나 같은 원소의 개수를 저장할 변수

        # 배열로 나타냈을 경우 각 행에서 중간점을 나눈 몫을 구하고, N과 비교하여 작은 값을 선택한 뒤, 모든 행에 대한 결과를 더해준다.
        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count < k:
            start = mid + 1  # 중간점보다 작은 원소의 개수가 k보다 작으면 시작점을 중간점 +1로 업데이트

        else:
            end = mid - 1  # 중간점보다 작거나 같은 원소의 개수가 k보다 크거나 같으면 끝점을 중간점 -1로

    return start  # 시작점이 k번재 원소인 B[k]의 값이므로, 시작점을 반환


n = int(input())
k = int(input())

result = find_B_k(n, k)
print(result)

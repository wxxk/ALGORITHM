import sys
sys.stdin = open('2231.txt')

N = int(input()) 
result = 0

for i in range(1, N+1):                 # N까지 모든 수를 비교(N = 216일 때)
    list_N = list(map(int, str(i)))     # 각 자리수의 합을 구하기 위한 list [2, 1, 6] = 9
    sum_N = i + sum(list_N)             # N + 각 자리수 합 i +(9) = 216 / i가 198이 되면 216이 됩니다.
    if sum_N == N:                      # 더했을 때 같으면
        result = i                      # i 값 저장
        break
print(result)
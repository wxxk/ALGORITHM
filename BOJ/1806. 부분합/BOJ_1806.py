import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
INF = sys.maxsize

n, s = map(int, input().split())
number = list(map(int, input().split()))
p1, p2 = 0, 0
L = INF
snum = 0

while True:
    # 합이 S이상인 경우
    if snum >= s:
        # 길이 비교해서 길이 저장
        L = min(L, p2 - p1)
        snum -= number[p1]
        # 왼쪽 한칸씩 이동하면서 어디까지 줄어드나 확인
        p1 += 1
    elif p2 == n:
        break
    else:
        # 합이 넘지 않으면 오른쪽으로 이동
        snum += number[p2]
        p2 += 1

if L == INF:
    print(0)
else:
    print(L)

"""
swap이 한번도 일어나지 않는 루프가 언제인지 찾는 문제
swap이 한번도 일어나지 않음 => 이미 모든 데이터가 정렬 되었다.
1. 안쪽 for문은 1에서 n-j까지 왼쪽에서 오른쪽으로 이동하면서 swap
2. 이는 특정 데이터가 안쪽 푸르에서 swap의 왼쪽으로 이동할 수 있는 최대 거리 1
3. 데이터 정렬 전 index와 정렬 후 index를 비교해서 왼쪽으로 가장 많이 이동한 값을 찾기
"""
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    num = int(input())
    arr.append((num, i))  # num과 정렬 전 index 저장

arr.sort()  # 정렬

"""
data : 1  2  3  5 10
bidx : 1  3  4  2  0
aidx : 0  1  2  3  4
move : 1  2  2 -1 -4 
"""

answer = 0
for i in range(n):
    # 정렬 전 idx - 정렬 후 idx의 최대값을 저장
    if arr[i][1] - i > answer:
        answer = arr[i][1] - i

print(answer + 1)

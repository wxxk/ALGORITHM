from heapq import heappush, heappop
from queue import PriorityQueue
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
card = []

for i in range(n):
    nums = int(input())
    heappush(card, nums)

answer = 0

while len(card) > 1:
    num_1 = heappop(card)
    num_2 = heappop(card)
    temp = num_1 + num_2
    answer += temp
    heappush(card, temp)

print(answer)

# 최대 힙
# heapq에서는 최대 힙을 제공하지 않는다.
# 따라서 부호를 변경하는 방법을 사용해서 최대 힙을 구현한다.
# 부호를 바꿔서 최소 힙에 넣어준 뒤 최솟값부터 pop을 해줄 때 다시 부호를 바꿔주면 최대 힙과 동일하다.
from heapq import heappop, heappush
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not q:
            print(0)
        else:
            print(-heappop(q))
    else:
        heappush(q, -x)

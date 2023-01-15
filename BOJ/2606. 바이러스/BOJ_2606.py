# 1. DFS를 시작할 노드를 정한 후 사용할 자료구조 초기화 하기
# (1). 원본 그래프
# (2). 인접 리스트로 표현
# (3). 방문 리스트
# (4). 스택 자료구조에 시작점을 삽입

# 2. 스택에서 노드를 꺼낸 후 노드의 인접 노드를 다시 스택에 삽입하기
# (1). 스택에서 노드를 꺼내면서 탐색 순서에 꺼낸 노드를 기록
# (2). 인접리스트
# (3). 대상 노드의 인접 노드를 스택에 삽입
# (4). 노드를 삽입하며 방문 리스트 체크

# 3. 스택 자료구조에 값이 없을 때 까지 반복

import sys

sys.stdin = open("input.txt")


def DFS(v):
    stack = [v]
    visited[v] = True

    while stack:
        cur = stack.pop()
        for adj in matrix[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)


input = sys.stdin.readline
n = int(input())
m = int(input())
matrix = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    matrix[s].append(e)
    matrix[e].append(s)
visited = [False] * (n + 1)

DFS(1)

print(sum(visited) - 1)

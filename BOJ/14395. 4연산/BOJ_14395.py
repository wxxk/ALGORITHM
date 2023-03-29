from collections import deque
import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, t = map(int, input().split())
visited = set()  # 방문한 수 저장
q = deque()  # BFS
q.append((n, ""))  # 뒤에는 연산의 기록
visited.add(n)  # n을 방문 처리
MAX = 10e9

if n == t:  # n이랑 t가 같으면
    print(0)  # 출력

elif t == 0:  # t가 0이면
    # n - n 으로 t를 만들 수 있기 때문에
    print("-")  # - 출력 후 종료

else:
    while q:
        x, clip = q.popleft()

        if x == t:
            print(clip)
            break

        if 0 <= x * x < MAX and x * x not in visited:
            visited.add(x * x)
            q.append((x * x, clip + "*"))

        if 0 <= x + x < MAX and x + x not in visited:
            visited.add(x + x)
            q.append((x + x, clip + "+"))

        if x // x not in visited:
            visited.add(x // x)
            q.append((x // x, clip + "/"))
    else:
        print(-1)

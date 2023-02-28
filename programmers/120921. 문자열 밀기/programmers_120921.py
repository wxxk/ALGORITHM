from collections import deque

A = "abc"
B = "abc"

if A == B:
    print(0)
else:
    A = deque(A)
    cnt = 1

    while True:
        if cnt == len(A):
            print(-1)
            break

        A.appendleft(A.pop())
        if ("".join(A)) == B:
            print(cnt)
            break
        else:
            cnt += 1

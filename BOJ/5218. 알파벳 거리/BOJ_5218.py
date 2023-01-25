import sys

sys.stdin = open("input.txt")

T = int(input())

for _ in range(T):

    a, b = map(list, input().split())
    len_list = len(a)
    result = []
    for i in range(len_list):
        if ord(b[i]) >= ord(a[i]):
            result.append(ord(b[i]) - ord(a[i]))
        else:
            result.append((ord(b[i]) + 26) - ord(a[i]))

    print("Distances: ", end="")
    print(*result)

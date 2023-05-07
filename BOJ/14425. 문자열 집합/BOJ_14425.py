import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dict = {}
cnt = 0

for _ in range(n):
    word = str(input())

    dict[word] = 1 + dict.get(word, 0)

    # if word in dict:
    #     dict[word] += 1
    # else:
    #     dict[word] = 1

for _ in range(m):
    word = str(input())

    if word in dict:
        cnt += 1

print(cnt)

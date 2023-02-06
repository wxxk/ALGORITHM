import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
dict_1 = {}

for i in range(1, n + 1):
    word = input().strip()
    dict_1[i] = word
    dict_1[word] = i

for i in range(m):
    quest = input().strip()
    if quest.isdigit():
        print(dict_1[int(quest)])
    else:
        print(dict_1[quest])

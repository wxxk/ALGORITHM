import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

word = input().strip()
bomb = list(input().strip())

result = []

for i in word:
    result.append(i)
    if result[-len(bomb) :] == bomb:
        for _ in range(len(bomb)):
            result.pop()

if result:
    print("".join(result))
else:
    print("FRULA")

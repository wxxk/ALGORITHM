import sys

sys.stdin = open("input.txt")

word = input()
count = 0

for i in word:
    print(i, end="")
    count += 1
    if count == 10:
        print()
        count = 0

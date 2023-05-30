import sys

sys.stdin = open("input.txt")

num = input()
result = [0] * 10

for n in num:
    n = int(n)

    if n == 6 or n == 9:
        if result[6] >= result[9]:
            result[9] += 1
        else:
            result[6] += 1

    else:
        result[n] += 1

print(max(result))

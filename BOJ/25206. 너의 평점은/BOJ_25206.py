import sys

# sys.stdin = open("input.txt")

dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

result = 0
total = 0

for _ in range(20):
    data = input().split()

    if data[2] == "P":
        continue

    total += float(data[1])
    result += float(data[1]) * dic[data[2]]

answer = result / total

print(format(answer, ".6f"))

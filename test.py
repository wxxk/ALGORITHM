import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
infos = []

while True:
    name, age, weight = map(str, input().split())

    if name == "#":
        break

    if int(age) > 17 or int(weight) >= 80:
        print(f"{name} Senior")

    else:
        print(f"{name} Junior")

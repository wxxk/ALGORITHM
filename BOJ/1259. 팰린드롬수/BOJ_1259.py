import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

while True:
    num = int(input())
    if num == 0:
        break
    num = str(num)

    if num[-1::-1] == num:
        print("yes")
    else:
        print("no")

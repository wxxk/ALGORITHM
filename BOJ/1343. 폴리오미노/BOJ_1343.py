import sys

sys.stdin = open("input.txt")

board = input().split(".")
result = ""
# print(board)

for i in board:
    # print(len(i) % 2)
    if len(i) % 2 != 0:
        print(-1)
        break
    if len(i) > 3:
        if len(i) % 4:
            result += "AAAA" * (len(i) // 4)
            result += "BB"
        else:
            result += "AAAA" * (len(i) // 4)

    elif len(i):
        result += "BB"
    result += "."

else:
    print(result[:-1])

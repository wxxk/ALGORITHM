quiz = ["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]
answer = []
for i in quiz:
    cal = i.split(" ")
    for j in range(0, len(cal), 2):
        cal[j] = int(cal[j])

    if cal[1] == "-":
        if cal[0] - cal[2] == cal[4]:
            answer.append("O")
        else:
            answer.append("X")
    else:
        if cal[0] + cal[2] == cal[4]:
            answer.append("O")
        else:
            answer.append("X")

print(answer)

common = [2, 4, 8]

num = common[1] - common[0]

if common[2] == num + common[1]:
    answer = common[len(common) - 1] + num
else:
    num = common[1] // common[0]
    answer = common[len(common) - 1] * num

print(answer)

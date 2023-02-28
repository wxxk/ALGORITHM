array = [1, 5, 2, 6, 3, 7, 4]
commends = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []
for commend in commends:
    i = commend[0] - 1
    j = commend[1]
    k = commend[2] - 1

    arr = sorted(array[i:j])
    answer.append(arr[k])

print(answer)

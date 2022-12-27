arr = [1, 1, 3, 3, 0, 1, 1]
answer = []

for i in range(len(arr)):
    if not answer:
        answer.append(arr[i])
    elif arr[i] != arr[i - 1]:
        answer.append(arr[i])

print(answer)

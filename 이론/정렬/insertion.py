num = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(num) - 1):
    for j in range(i, -1, -1):
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
        else:
            break

print(num)

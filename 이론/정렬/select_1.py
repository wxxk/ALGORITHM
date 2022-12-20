num = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(num)):
    min = i

    for j in range(i + 1, len(num)):
        if num[min] > num[j]:
            min = j

    if num[i] > num[min]:
        num[i], num[min] = num[min], num[i]

print(num)

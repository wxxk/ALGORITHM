num = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(len(num) - 1):

    for j in range(len(num) - 1 - i):

        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
print(num)

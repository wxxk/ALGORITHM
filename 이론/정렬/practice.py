# bubble
bubble = [7, 2, 6, 1, 4, 8, 9, 3, 10, 5]

for i in range(len(bubble) - 1):
    for j in range(len(bubble) - 1 - i):
        if bubble[j] > bubble[j + 1]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print(bubble)


for i in range(len(bubble) - 1):
    for j in range(len(bubble) - 1 - i):
        if bubble[j + 1] > bubble[j]:
            bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
print(bubble)

####################################################################

select = [7, 2, 6, 1, 4, 8, 9, 3, 10, 5]

for i in range(len(select)):
    min = i
    for j in range(i + 1, len(select)):
        if select[min] > select[j]:
            min = j
    if select[i] > select[min]:
        select[i], select[min] = select[min], select[i]
print(select)


for i in range(len(select)):
    max = i
    for j in range(i + 1, len(select)):
        if select[j] > select[max]:
            max = j
    if select[max] > select[i]:
        select[max], select[i] = select[i], select[max]
print(select)

#######################################################################

insertion = [7, 2, 6, 1, 4, 8, 9, 3, 10, 5]

for i in range(len(insertion) - 1):
    for j in range(i, -1, -1):
        if insertion[j] > insertion[j + 1]:
            insertion[j], insertion[j + 1] = insertion[j + 1], insertion[j]
print(insertion)

for i in range(len(insertion) - 1):
    for j in range(i, -1, -1):
        if insertion[j + 1] > insertion[j]:
            insertion[j + 1], insertion[j] = insertion[j], insertion[j + 1]
print(insertion)

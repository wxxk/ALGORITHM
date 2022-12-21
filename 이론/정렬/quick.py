def quick(data, start, end):
    if start >= end:
        return

    key = start
    i = start + 1
    j = end

    while i <= j:
        while data[i] <= data[key]:
            i += 1
        while (data[j] >= data[key]) and j > start:
            j -= 1
        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[j], data[i] = data[i], data[j]

    quick(data, start, j - 1)
    quick(data, j + 1, end)


data = [7, 2, 6, 1, 4, 8, 9, 3, 10, 5]
number = 10

quick(data, 0, number - 1)

print(data)

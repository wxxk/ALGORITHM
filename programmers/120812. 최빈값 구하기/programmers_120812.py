def solution():
    dict = {}
    cnt = 0
    for i in array:
        dict[i] = dict.get(i, 0) + 1

    max_key = max(dict, key=dict.get)
    max_value = max(dict.values())

    for i, j in dict.items():
        if max_value == j:
            cnt += 1

    if cnt > 1:
        print(-1)
    else:
        print(max_key)


array = [1, 1, 2, 2]

solution()

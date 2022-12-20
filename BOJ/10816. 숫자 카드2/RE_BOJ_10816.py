card = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
finds = [10, 9, -5, 2, 3, 4, 5, -10]
dict = {} # card 정수 값의 갯수를 담을 딕셔너리

for num in card:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1

for i in finds:
    if i in dict:
        print(dict[i], end= ' ')
    else:
        print(0, end= ' ')
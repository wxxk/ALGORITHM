ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
result =[]
burger = []
cnt = 0

for i in ingredient:
    burger.append(i)
    if burger[-4:] == [1, 2, 3, 1]:
        cnt += 1

        for i in range(4):
            burger.pop()

print(cnt)

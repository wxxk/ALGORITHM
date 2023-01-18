numbers = [1, 2, 3, 4, 6, 7, 8, 0]
answer = 0

for i in range(10):
    if not i in numbers:
        answer += i

print(answer)

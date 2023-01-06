from collections import deque

food = [1, 7, 1, 2]

result = deque()
result.append(0)
answer = ""

for i in range(1, len(food)):
    if food[i] % 2 != 0:
        food[i] -= 1

for j in range(len(food) - 1, 0, -1):
    for k in range(food[j] // 2):
        result.append(j)
        result.appendleft(j)

for l in result:
    answer += str(l)

print(answer)

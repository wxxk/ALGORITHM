numbers = [2, 3, 3, 5]
answer = [0] * len(numbers)
stack = []

for i in range(len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
        answer[stack.pop()] = numbers[i]
    stack.append(i)
while stack:
    answer[stack.pop()] = -1

print(answer)

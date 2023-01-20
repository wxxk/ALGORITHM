from collections import deque

numbers = [1, 2, 3]
direction = "right"
numbers = deque(numbers)

if direction == "right":
    numbers.rotate(1)
else:
    numbers.rotate(-1)
print(list(numbers))

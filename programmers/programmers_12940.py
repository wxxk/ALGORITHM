n, m = 3, 12
a, b = max(n, m), min(n, m)
answer = []

while b > 0:
    a, b = b, a % b

answer.append(a)
answer.append((n * m) // a)

print(answer)

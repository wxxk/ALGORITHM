n = 4
answer = 0

for i in range(1, n + 1):
    if (i * 6) % n == 0:
        answer += 1
        break
    else:
        answer += 1

print(answer)

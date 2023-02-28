n = 5

prime = [False, False] + [True] * (n - 1)

result = []

for i in range(2, n + 1):
    if prime[i]:
        result.append(i)
        for j in range(2 * i, n + 1, i):
            prime[j] = False

print(result)
print(len(result))

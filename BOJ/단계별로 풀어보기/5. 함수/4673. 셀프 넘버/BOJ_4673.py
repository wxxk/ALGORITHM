numbers = list(range(1, 10001))
generated_numbers = []

for i in numbers:
    total = 0
    total = i + sum(map(int, str(i)))
    generated_numbers.append(total)

self_numbers = sorted(set(numbers) - set(generated_numbers))

for i in self_numbers:
    print(i)
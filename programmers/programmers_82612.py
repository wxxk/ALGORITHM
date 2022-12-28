price = 3
money = 20
count = 4

sum = 0

for i in range(count):
    sum += price * (i + 1)

if sum - money > 0:
    print(sum - money)
else:
    print(0)

x = 13

arr = str(x)
num = 0

for i in arr:
    num += int(i)

if x % num == 0:
    print("true")
else:
    print("false")

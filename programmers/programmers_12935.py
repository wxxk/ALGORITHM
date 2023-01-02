arr = [4,3,2,1]

min = arr[0]
for i in arr:
    if min > i:
        min, i = i, min

arr.remove(min)

if arr:
    print(arr)
else:
    print([-1])
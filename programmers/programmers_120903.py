s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
cnt = 0

for i in s1:
    for j in s2:
        if i == j:
            cnt += 1

print(cnt)

s1 = ["a", "b", "c"]
s2 = ["com", "b", "d", "p", "c"]
cnt = 0

for i in s1:
    if i in s2:
        cnt += 1

print(cnt)

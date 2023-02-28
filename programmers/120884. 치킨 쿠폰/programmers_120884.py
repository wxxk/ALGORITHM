chicken = 1081
answer = 0

while chicken >= 10:
    temp = chicken // 10
    answer += temp
    chicken = chicken % 10 + temp

print(answer)

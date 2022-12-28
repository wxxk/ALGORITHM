phone_number = "01033334444"
# re = 0

# re = len(phone_number) - 4

# for i in range(re):
#     phone_number = phone_number.replace(phone_number[i], "*")

# print(phone_number)

answer = "*" * (len(phone_number) - 4)
answer += phone_number[-4:]

print(answer)

my_string = "hello"
num1 = 1
num2 = 2
answer = ""
my_string = list(my_string)

my_string[num1], my_string[num2] = my_string[num2], my_string[num1]

for i in my_string:
    answer += i

print(answer)

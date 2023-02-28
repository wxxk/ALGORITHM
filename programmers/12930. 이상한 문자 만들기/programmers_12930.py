s = "try hello world"
answer = ""
word = s.split()

for i in word:
    for j in range(len(i)):
        if j % 2 == 0:
            answer += i[j].upper()
        else:
            answer += i[j].lower()

    answer += " "

print(answer)

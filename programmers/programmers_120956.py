from itertools import permutations

word = ["aya", "ye", "woo", "ma"]
com = []
babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
answer = 0

for i in range(len(word)):
    # com.append(list(map("".join, permutations(word, i + 1))))
    for j in permutations(word, i + 1):
        com.append(j)

for i in babbling:
    if i in com:
        answer += 1

print(answer)

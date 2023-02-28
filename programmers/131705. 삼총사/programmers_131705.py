from itertools import combinations

answer = 0
number = [-3, -2, -1, 0, 1, 2, 3]

for i in combinations(number, 3):
    if sum(i) == 0:
        answer += 1

print(answer)

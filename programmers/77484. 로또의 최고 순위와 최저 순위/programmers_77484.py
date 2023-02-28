lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
nums = []
cnt = lottos.count(0)
rank = [6, 6, 5, 4, 3, 2, 1]
answer = []

for i in lottos:
    for j in win_nums:
        if i == j:
            nums.append(i)


max = len(nums) + cnt
min = len(nums)

answer.append(rank[max])
answer.append(rank[min])
print(answer)

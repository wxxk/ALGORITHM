import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
result = []
for _ in range(n):
    team = input().strip()
    members = []
    t = int(input())

    for _ in range(t):
        name = input().strip()
        members.append(name)
    members = sorted(members)
    for i in members:
        dic[i] = team

for _ in range(m):
    temp = str(input().strip())
    quiz = int(input())

    if quiz == 0:
        for n, t in dic.items():
            if temp == t:
                result.append(n)
    else:
        result.append(dic.get(temp))

for res in result:
    print(res)

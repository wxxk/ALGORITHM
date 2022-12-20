import sys
sys.stdin = open ('1302.txt')

N = int(input())
dict = {}

for i in range(N):
    book = input()

    if book in dict:
        dict[book] += 1
    else:
        dict[book] = 1

num = max(dict.values())
list_dict = []

for i in dict:
    if num == dict[i]:
        list_dict.append(i)

list_dict.sort()
print(list_dict[0])
import sys
sys.stdin = open('10809.txt')

N = list(map(str, input()))
numbers_list = [-1] * 26

for i in range(len(N)):
    numbers_list[ord(N[i])-97] = N.index(N[i])

for j in range(len(numbers_list)):
    print(numbers_list[j], end= ' ')
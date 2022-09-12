import sys
sys.stdin = open('1764.txt')

n, m = map(int, input().split())

list_n = [input() for _ in range(n)]
list_m = [input() for _ in range(m)]

duplicate = list(set(list_n) & set(list_m))

print(len(duplicate))
for i in sorted(duplicate):
    print(i)
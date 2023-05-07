from itertools import combinations
import sys

input = sys.stdin.readline
sys.stdin = open("input.txt")

while True:
    s = list(map(int, input().split()))

    if s[0] == 0:
        break
    del s[0]

    for i in combinations(s, 6):
        print(*i)
    print()

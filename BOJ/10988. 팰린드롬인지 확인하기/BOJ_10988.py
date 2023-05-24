import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

s = input()
re = ""

if s == s[::-1]:
    print(1)
else:
    print(0)

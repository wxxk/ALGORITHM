import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
n = n // 4
for i in range(n // 1):
    print("long", end=" ")
print("int")

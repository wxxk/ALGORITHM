import sys
sys.stdin = open ('2588.txt')

A = int(input())
B = input()

for i in range(2, -1, -1):
    print(A * int(B[i]))
print(A*int(B))
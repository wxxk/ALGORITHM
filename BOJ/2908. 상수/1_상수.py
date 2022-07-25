# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(str, input().split())

if A[::-1] > B[::-1]:
    print(A[::-1])
elif A[::-1] < B[::-1]:
    print(B[::-1])
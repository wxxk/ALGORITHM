import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

word = list(input().rstrip())
bomb = list(input())

result = []

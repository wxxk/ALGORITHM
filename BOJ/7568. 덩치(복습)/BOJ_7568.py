import sys
sys.stdin = open('7568.txt')

T = int(input())
rank_list = []

for i in range(1, T+1):
     rank_list.append(list(map(int, input().split())))

for j in rank_list:
     rank = 1
     for k in rank_list:
          if j[0] < k[0] and j[1] < k[1]:
               rank += 1
     print(rank, end=' ')
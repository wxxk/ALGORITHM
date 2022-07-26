import sys
sys.stdin = open ('2846.txt')

n = int(input())
num = list(map(int, input().split()))
diff = 0

for i in range(0, n): # 1 2 1 4 6
    for j in range(i + 1, n): 
        if num[j] - num[j-1] > 0: 
            diff = max(diff, num[j] - num[i])
        else:
            break

print(diff)
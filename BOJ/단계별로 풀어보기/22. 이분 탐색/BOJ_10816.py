import sys
sys.stdin = open('10816.txt')

import sys
N = int(sys.stdin.readline())
N_numbers = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_numbers = list(map(int, sys.stdin.readline().split()))
result =[]

for i in range(len(M_numbers)): 
    print(N_numbers.count(M_numbers[i]), end=' ')
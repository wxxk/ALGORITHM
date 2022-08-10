import sys  # sys모듈 읽어들이기
sys.stdin =open('15552.txt')

t = int(sys.stdin.readline())

for i in range(1, t+1):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
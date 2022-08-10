import sys
sys.stdin = open('10951.txt')

while True:
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A+B)
    except:
        break
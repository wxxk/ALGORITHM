import sys
sys.stdin = open('8958.txt')
T = int(input())

for tc in range(T):
    quiz = list(input())
    cnt = 0
    sum = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0

    print(sum)
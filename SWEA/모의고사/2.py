import sys
sys.stdin = open('2.txt')
T = int(input())

for i in range(1, T+1):
    word = list(input())
    word.reverse()
    result = ''

    for j in range(len(word)):
        if word[j] == 'b':
            word[j] = 'd'
        elif word[j] =='d':
            word[j] = 'b'
        elif word[j] == 'p':
            word[j] = 'q'
        elif word[j] == 'q':
            word[j] = 'p'
        result = ''.join(word)
    print(f'#{i} {result}')
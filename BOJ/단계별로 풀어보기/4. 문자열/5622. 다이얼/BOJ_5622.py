import sys
sys.stdin = open('5622.txt')

dict = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
result = 0

for i in range(len(word)):
    for j in dict:
        if word[i] in j:
            result += dict.index(j)+3

print(result)
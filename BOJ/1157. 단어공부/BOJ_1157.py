import sys
sys.stdin = open('1157.txt')

word = input().upper()
word_list = list(set(word))
num = []

for i in word_list:
    count = word.count(i)
    num.append(count)

if (num.count(max(num))) > 1:
    print('?')

else:
    print(word_list[(num.index(max(num)))])
import sys
sys.stdin = open ('2941.txt')

croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

for i in range(len(croa)):
    if croa[i] in word:
        word =word.replace(croa[i], ' ')
    else:
        continue

print(len(word))
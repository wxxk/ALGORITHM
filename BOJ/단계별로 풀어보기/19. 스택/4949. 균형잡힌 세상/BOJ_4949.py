import sys
sys.stdin = open('4949.txt')

while True:
    words = input()
    if words == '.':
        break

    PS = []

    for i in words:
        if i == '[' or i == '(':
            PS.append(i)

        elif i == ']' :
            if len(PS) != 0 and PS[-1] == '[' :
                PS.pop()
            else:
                PS.append(i)
                break

        elif i == ')':
            if len(PS) != 0 and PS[-1] == '(' :
                PS.pop()
            else:
                PS.append(i)
                break

    if len(PS) == 0:
        print('yes')
    else:
        print('no')
import sys
sys.stdin = open('4949.txt')

while True:
    words = input()
    if words == '.':
        break
    
    PS = []

    # temp = True

    for i in words:
        if i == '[' or i == '(':
            PS.append(i)

        elif i == ']' :
            if len(PS) != 0 and PS[-1] == '[' :
                PS.pop()
            else:
                PS.append(i)
                # temp = False
                break

        elif i == ')':
            if len(PS) != 0 and PS[-1] == '(' :
                PS.pop()
            else:
                PS.append(i)
                # temp = False
                break

    if not PS :
        print('yes')
    else:
        print('no')

    # if temp == True and not PS:
    #     print('yes')
    # else:
    #     print('no')
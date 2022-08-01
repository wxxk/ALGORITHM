import sys
sys.stdin = open ('5.txt')

T = int(input())

for i in range(1, T+1):
    numbers = input()

    if '-' in numbers:
        numbers = numbers.replace('-', '')
        if numbers.startswith(('3', '4', '5', '6', '9')) and len(numbers) == 16:
            print(f'#{i} {1}')
        else:
            print(f'#{i} {0}')
    
    else:
        if numbers.startswith(('3', '4', '5', '6', '9')) and len(numbers) == 16:
            print(f'#{i} {1}')
        else:
            print(f'#{i} {0}')

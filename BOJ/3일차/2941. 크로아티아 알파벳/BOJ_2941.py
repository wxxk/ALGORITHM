import sys
sys.stdin = open('2941.txt')
T = int(input())

for i in range(1, T+1):
    word = input()
    
    # 단어에 크로아티아 문자가 있는 것을 확인하기 위한 크로아티아 알파벳 리스트를 생성
    word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    

    for i in word_list: # ljes=njak
        # 크로아티아 알파벳리스트와 단어를 비교하여 크로아티아 단어를 임의의 문자로 변경
        if i in word:
            word = word.replace(i, '*')

    # 크로아티아 문자가 변환된 단어의 길이를 센다
    print(len(word)) # ex) ljes=njak -> *e**ak 
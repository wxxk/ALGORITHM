numbers = list(range(1,101))
remove_list=[]    #생성자 리스트
for num in numbers:
    for n in str(num):
        num += int(n)
    if num <= 100:
        remove_list.append(num)
for remove_num in set(remove_list):
    numbers.remove(remove_num)
for self_num in numbers:
    print(self_num)

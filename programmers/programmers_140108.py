def solution(s):
    answer = 0
    str_dic = {}
    text = ""
    for i in s:
        if not str_dic:
            str_dic[i] = 1
            text = i
        else:
            if text == i:
                str_dic[i] += 1
            else:
                if str_dic.get("other"):
                    str_dic["other"] += 1
                else:
                    str_dic["other"] = 1

        if len(str_dic) == 2 and str_dic[text] == str_dic["other"]:
            str_dic = {}
            answer += 1

    if str_dic:
        answer += 1

    return answer


s = "abracadabra"
print(solution(s))

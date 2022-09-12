participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]

    else: 
        return participant[len(participant)-1]

print(solution(participant, completion))
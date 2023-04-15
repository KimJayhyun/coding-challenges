## https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

##############################################################################

def solution(participant, completion):
    answer = ''

    dic_completion = {}

    for name in completion:
        if hash(name) not in dic_completion.keys():
            dic_completion[ hash(name) ] = [name]
        else :
            dic_completion[ hash(name) ].append(name)

    for name in participant:
        if hash(name) not in dic_completion.keys():
            answer = name
        else :
            if len( dic_completion[ hash(name) ] ) == 0:
                answer = name
            else :
                dic_completion[ hash(name) ].remove(name)

    for v in dic_completion.values():
        if len(v) == 1:
            answer = v

    return answer
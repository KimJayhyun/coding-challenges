# https://programmers.co.kr/learn/courses/18/lessons/1878

def solution(v):
    answer = []

    x_list = []
    y_list = []

    for e in v :
        if e[0] not in x_list:
            x_list.append(e[0])
        else :
            x_list.remove(e[0])

        if e[1] not in y_list:
            y_list.append(e[1])
        else :
            y_list.remove(e[1])

    answer = [x_list[0], y_list[0]]
    return answer
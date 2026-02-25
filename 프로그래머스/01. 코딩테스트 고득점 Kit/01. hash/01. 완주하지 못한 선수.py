# https://school.programmers.co.kr/learn/courses/30/lessons/42576


def solution(participant, completion):
    participant_dict = {}
    for name in participant:
        if name not in participant_dict:
            participant_dict[name] = 1
        else:
            participant_dict[name] += 1

    completion_dict = {}
    for name in completion:
        if name not in completion_dict:
            completion_dict[name] = 1
        else:
            completion_dict[name] += 1

    for name in participant:
        if name not in completion_dict:
            return name

        if participant_dict[name] != completion_dict[name]:
            return name

# https://programmers.co.kr/learn/courses/30/lessons/42860

# 알파벳은 26개

def distance(c):
    code_A = ord("A")
    code_Z = ord("Z")
    code = ord(c)

    x = abs(code - code_A)
    y = abs(code_Z - code) + 1

    return x if x < y else y

def solution(name):
    answer = 0


    for c in name:
        answer += distance(c)

    x = 0
    y = 0
    
    for i in range(len(name)):
        if name[i] != "A":
            x = i

    for i in range(-1, -1 * len(name), -1):
        if name[i] != 'A':
            y = i

    y = -1 * y

    temp = x if x < y  else y

    return answer + temp

print(solution("JAN"))
print(solution("JEROEN"))

print("JAN"[-3])

for i in range(-1 , -2 , -1):
    print(i)
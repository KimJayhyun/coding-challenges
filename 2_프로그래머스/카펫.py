# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    answer = []
    num = brown + yellow
    temp = int( (brown + yellow) ** (1/2))

    
    for i in range(3, temp + 1):
        if num % i == 0:
            x = i
            y = num / x        

            if x + y == int(brown / 2) + 2:
            #  or x + y == int(yellow / 2) + 2:
                break
                
    answer = [
        y if y >= x else x,
        x if y>= x else y
    ] 

    return answer

# print(int(48 ** (1/2)))

# for i in range(11, 3, -1):
#     print(i)
# 
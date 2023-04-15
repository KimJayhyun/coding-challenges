def solution(n):
    answer = 0
    m = n
    while True:
        temp = m % 10 
        answer += temp
        m = int(m/10)
        if m == 0:
            break
    
    return answer


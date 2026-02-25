## https://programmers.co.kr/learn/courses/30/lessons/42839

def isPrime(num):
    if num == 1:
        return False

    r = int(num ** (1/2))

    for i in range(2, r + 1):
        if num % i == 0:
            return False

    return True

def makeBinaryNum(num, length):
    if num == 0:
        return length * "0"

    binary = ""
    temp = num

    while(temp >= 1):
        x = temp % 2     
        binary = str(x) + binary
        temp //= 2
    
    temp = length - len(binary)

    binary = "0" * temp + binary

    return binary

def solution(numbers):
    answer = 0
    
    dic_answer = {}

    length = len(numbers)

    for i in range(1, 2 ** (length)):
        x = makeBinaryNum(i, length)
        
        temp = []

        for j in range(len(x)):
            if x[j] == "1":
                temp.append(numbers[j])

        
        

        



solution("01234")

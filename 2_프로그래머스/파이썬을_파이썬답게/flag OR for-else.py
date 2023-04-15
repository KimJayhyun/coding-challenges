# def isSquare(num):
#     cnt = 0
    
#     for i in range(1, num + 1):
#         if num % i == 0:
#             cnt += 1
    
#     if cnt % 2 == 1:
#         return True
#     else:
#         return False
        

# pi = 1
# answer = ""

# for i in range(5):
#     a = int(input())    
    
#     pi *= a
    
#     if isSquare(pi):
#         answer = 'found'
#         break
#     else :
#         answer = "not found"
    
# print(answer)
        
import math

if __name__ == '__main__':
    numbers = [int(input()) for _ in range(5)]
    multiplied = 1
    for number in numbers:
        multiplied *= number
        if math.sqrt(multiplied) == int(math.sqrt(multiplied)):
            print('found')
            break
    else:
        print('not found')    
    

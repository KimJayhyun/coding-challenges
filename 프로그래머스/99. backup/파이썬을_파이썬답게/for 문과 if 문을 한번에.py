# def solution(mylist):
#     answer = []

#     for n in mylist:
#         if n % 2 == 0:
#             answer.append(n * n)
#         else :
#             continue        


#     return answer

def solution(mylist):
    answer = [number**2 for number in mylist if number % 2 == 0]
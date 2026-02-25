# https://programmers.co.kr/learn/courses/18/lessons/1877

# def solution(arr):
#     answer = False
#     temp = max(arr)
#     length = len(arr)
    

#     if length != temp:
#         return False

#     for i, n in enumerate(arr):
#         if i == length - 1:
#             return True
#         if n > temp:
#             return False

#         if n == arr[i + 1]:
#             return False
    
#     return True

def solution(arr):
    
    if max(arr) != len(arr):
        return False

    temp = [0 for _ in range(100000)]
    
    for n in arr:
        if temp[n-1] == 1:
            return False
        else :
            temp[n-1] = 1
    return True

## 1. 체크 List 하나 추가
#            1 2 3 4
# 4 1 2 3 => 1 1 1 1 

## 2. 정렬 후 Check

                
    

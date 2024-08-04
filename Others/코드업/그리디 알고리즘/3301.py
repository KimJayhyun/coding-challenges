## https://codeup.kr/problem.php?id=3301

x = int(input())

# x = 54520

# num = [10, 50, 100, 500, 1000, 5000, 10000, 50000]

answer = 0

while(x != 0):        
    t1 = x - 10 
    t2 = x - 50 
    t3 = x - 100
    t4 = x - 500
    t5 = x - 1000
    t6 = x - 5000
    t7 = x - 10000
    t8 = x - 50000

    arr = [t1, t2, t3, t4, t5, t6, t7, t8]

    # print(arr)

    for t in arr:
        if t >= 0:
            min = t
            break    

    for i in range(1, len(arr)):
        if arr[i] < 0 :
            continue
        if min > arr[i]:
            min = arr[i]

    x = min
    # break

    answer += 1

print(answer)
## https://codeup.kr/problem.php?id=3120

# # +- 1, 5, 10 버튼 6개
# x, y = input().split(" ")
# x = int(x)
# y = int(y)

y = 34
x = 7

temp = y - x
answer = 0 
num = [-1, -5, -10, 1, 5, 10]

while(temp != 0):
    t1 = abs(temp - 1)
    t2 = abs(temp - 5)
    t3 = abs(temp - 10)
    t4 = abs(temp + 1)
    t5 = abs(temp + 5)
    t6 = abs(temp + 10)

    # dic ={
    #     -1 : t1,
    #     -5 : t2,
    #     -10 : t3,
    #     1 : t4,
    #     5 : t5,
    #     10 : t6
    # }

    arr = [t1, t2, t3, t4, t5, t6]
    
    

    min = t1
    index = 0
    for i in range(1, 6):
        if min > arr[i] : 
            min = arr[i]
            index = i

    answer += 1
    temp += num[index]

print(answer)






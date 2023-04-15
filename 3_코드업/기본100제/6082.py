## 369 하기
# 33과 같이 두 번들어간 경우 두번 박수
# 박수는 X로 대체

num = int(input())
answer = ""
for i in range(1, num + 1):
    temp = str(i)
    trans = ""

    # temp = temp.replace('3', 'X')
    # temp = temp.replace('6', 'X')
    # temp = temp.replace('9', 'X')

    # answer = answer + temp + " "

    time = 0
    for j in range(len(temp)):
        if temp[j] == '3' or temp[j] == '6'or temp[j] == '9':
            time += 1            
            
    if time != 0:
        trans = "X" * time
    else :
        trans = temp
        
    answer = answer + trans + " "

print(answer)




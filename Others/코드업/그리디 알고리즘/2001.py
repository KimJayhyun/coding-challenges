## https://codeup.kr/problem.php?id=2001

p1 = int(input())
p2 = int(input())
p3 = int(input())

j1 = int(input())
j2 = int(input())

# p1 = 800
# p2 = 700
# p3 = 900

# j1 = 198
# j2 = 300

j = j1 if j1 < j2 else j2


p = p1 if p1 < p2 else p2 
p = p if p < p3 else p3

price = (p+j) * 1.1
print("{:.1f}".format(price))


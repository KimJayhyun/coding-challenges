# my_str = "bbaa"
# answer = ""
# my_list = list(my_str)
# my_list.sort()

# dic = {}
# for i, v in enumerate(my_list):
#     if v in dic.keys():
#         dic[v] += 1
#     else: 
#         dic[v] = 1

# max_cnt = max(dic.values())

# for k, v in dic.items():
#     if v == max_cnt:
#         answer += k

# print(answer)
import collections
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 9, 1, 2, 3, 3, 5, 2, 6, 8, 9, 0, 1, 1, 4, 7, 0]
answer = collections.Counter(my_list)

print(answer[1]) # = 4
print(answer[3])  # = 3
print(answer[100]) # = 0
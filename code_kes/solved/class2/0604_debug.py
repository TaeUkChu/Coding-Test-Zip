# 왜 틀렸는가
while True:
    num = input()
    if num == "0":
        break
    num = list(num)
    reverse_num = []
    n = len(num)

    
    for i in range(1, n+1):
        reverse_num.append(num[-i])
        
    num = "".join(num)
    reverse_num="".join(reverse_num)

    if num == reverse_num:
        print("yes")
    else:
        print("no")
    
        


# 원본
# while True:
#     num = list(input())
#     reverse_num = []
#     n = len(num)

#     if num[0] != '0': # n=3
#         for i in range(1, n+1):
#             # print("n이 3일 때 왜 틀렸는가", num[-i])
#             reverse_num.append(num[-i])
            
#         num = "".join(num)
#         reverse_num="".join(reverse_num)
#         # print("조합 비교", num, reverse_num)

#         if num == reverse_num:
#             print("yes")
#         else:
#             print("no")
#     else:
#         print("no")

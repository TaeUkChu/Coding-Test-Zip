# # 1

# import sys
# sys.setrecursionlimit(int(1e6)) # 재귀함수의 깊이 지정
# input= sys.stdin.readline 

# memo = {
#     0 : 0,
#     1 : 1,
#     2 : 1,
# }


# def fb(temp):
#     if not temp in memo:
#         memo[temp] = fb(temp-1) + fb(temp-2)
#     return memo[temp]

# n = input()
# for i in range(n):
#     temp = input()
    
#     if not temp:
#         print(1,0)
#     else:
#         fb(temp)
#         print(memo[temp-1], memo[temp]) # a,b = b, a+b

# # 2 

# import sys
# sys.setrecursionlimit(int(1e6))
# input = sys.stdin.readline

# memo={
#     0 : 0,
#     1 : 1,
#     2 : 1,
# }

# def fb(temp):
#     if not temp in memo:
#         memo[temp] = fb(temp-1) + fb(temp-2)
#     return memo[temp]

# n = input()
# for i in range(n):
#     temp = input()
#     if not temp:
#         print(1,0)
#     else:
#         fb(temp)
#         print(memo[temp-1], memo[temp])
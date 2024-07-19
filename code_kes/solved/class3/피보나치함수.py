# https://www.acmicpc.net/problem/1003

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

memo = {
    0 : 0,
    1 : 1,
    2 : 1,
}

def fb(temp):
    if not temp in memo:
        memo[temp] = fb(temp-1) + fb(temp-2)
    return memo[temp]

n = int(input())
for i in range(n):
    temp = int(input())
    if not temp:
        print('1 0')
    else:
        fb(temp)
        print(memo[temp-1], memo[temp]) # memo[temp-1] 0의 호출횟수,  memo[temp] 1의 호출 횟수인지?





# if n == 0:
        
#         zero += 1
#         return 0
    
#     elif n == 1:
#         one += 1
#         return 1
    
#     else:
#         return fb(n-1) + fb(n-2)

# n = int(input())



# for i in range(n):
#     one = 0
#     zero = 0
#     a = int(input())
#     fb(a)
#     print(zero, one)
    
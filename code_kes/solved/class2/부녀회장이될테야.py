# 문제 : https://www.acmicpc.net/problem/2775
# 정리 :

# import sys
# # ys.setrecursionlimit(1000000)
# input = sys.stdin.readline

people = 0
def Apt(idx,r):
    global people
    if idx == 0:
        people += r
    else:
        idx -= 1
        for i in range(1,r+1):
            Apt(idx, i)
        
t = int(input())
for i in range(t):
    idx = int(input())
    r = int(input())
    Apt(idx, r)
    print(f"{idx}층 {r}호 {people}명")
    print(people)
    people = 0
    

# else:
#         idx -= 1
#         for j in range(1,b+1): # == b * (b + 1) // 2
#             Apt(idx, j)


    

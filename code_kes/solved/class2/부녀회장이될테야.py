# 백준 최대공약수와 부녀회장이 될테야[브론즈1, 2775]
# 문제 : https://www.acmicpc.net/problem/2775
# 정리 :

# import sys
# sys.setrecursionlimit(1000000)
# input = sys.stdin.readline

def Apt(idx,r):
    global people, calls
    calls += 1
    
    if idx == 0:
        people += r
        
    else:
        idx -= 1
        for i in range(1,r+1):
            Apt(idx, i)
        
t = int(input())
people = 0
calls = 0

for i in range(t):
    idx = int(input())
    r = int(input())
    Apt(idx, r)
    print("People:", people)
    people = 0
    
print("재귀함수 호출횟수:", calls)    

# People: 37442160
# 재귀함수 호출횟수: 40116600


# print(f"{idx}층 {r}호 {people}명")
# else:
#         idx -= 1
#         for j in range(1,b+1): # == b * (b + 1) // 2
#             Apt(idx, j)


# 재귀함수 호출 횟수 측정
# def Apt(idx, r):
#     global people, calls
#     calls += 1  # 재귀 호출 횟수 증가
#     if idx == 0:
#         people += r
#     else:
#         idx -= 1
#         for i in range(1, r + 1):
#             Apt(idx, i)

# t = int(input())
# for _ in range(t):
#     idx = int(input())
#     r = int(input())
#     people = 0
#     calls = 0  # 재귀 호출 횟수 초기화
#     Apt(idx, r)
#     print("People:", people)
#     print("Calls:", calls)

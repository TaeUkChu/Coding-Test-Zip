# 1차, return 없이 memo에는 None 값만 저장됨

def Apt(idx,r):
    
    global people, calls
    calls += 1
    
    if (idx,r) in memo:    
        people += memo[(idx, r)]
    
    # 추가 조건 : 모든 층은 1호에 1명이 산다.
    elif r == 1:
        memo[(idx,r)] = 1 # memoization
        people += 1
        
    
    elif idx == 0:
        memo[(idx,r)] = r
        people += r
        
    else:
        idx -= 1
        for i in range(1,r+1):
            temp = Apt(idx, r)
            memo[(idx,r)] = temp # memoization
        
t = int(input())
people = 0
calls = 0
memo = {}  # memoization

for i in range(t):
    idx = int(input())
    r = int(input())
    Apt(idx, r)
    print(people)
    people = 0
    calls = 0
    
    print("People:", people)
    print("재귀함수 호출횟수:", calls)
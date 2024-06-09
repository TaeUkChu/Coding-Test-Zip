# 2차 조건식 별 계산 값을 return 하기

def Apt(idx,r):
    
    global calls
    calls += 1
    
    if (idx,r) in memo:    
        return memo[(idx, r)]
    
    # 추가 조건 : 모든 층은 1호에 1명이 산다.
    elif r == 1:
        memo[(idx,r)] = 1 # memoization
        return 1
        
    elif idx == 0:
        memo[(idx,r)] = r
        return r
        
    else:
        people = 0
        idx -= 1
        
        for i in range(1,r+1):
            temp = Apt(idx, i)
            memo[(idx,i)] = temp # memoization
            people += temp
        
        return people
        
t = int(input())
people = 0
calls = 0
memo = {}  # memoization

for i in range(t):
    idx = int(input())
    r = int(input())
    people = Apt(idx, r)
    print(people)
    
print("People:", people)
print("재귀함수 호출횟수:", calls)

# People: 37442160
# 재귀함수 호출횟수: 1367
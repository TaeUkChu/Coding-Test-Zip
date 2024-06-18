# 문제 : https://www.acmicpc.net/problem/7568

n = int(input())
body_li = []
answer = []

for i in range(n):
    h, kg = map(int, input().split())
    body = [h, kg]
    body_li.append(body)

N = len(body_li)

for i in range(N):
    temp = body_li[i]
    cnt = 0
    for j in range(N):
        if temp[0] < body_li[j][0] and temp[1] < body_li[j][1]:
            cnt += 1
    answer.append(cnt)

for i in answer:
    print(i+1 ,end=" ")
    
    
        
        
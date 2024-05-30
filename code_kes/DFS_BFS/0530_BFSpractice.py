# 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 정리 : https://velog.io/@uiseoo/DFSBFS-타겟넘버-Level-2
from collections import deque
number = [1,1,1,1,1]
target = 3
answer = 0
q =deque()
n = len(number) # 숫자배열의 크기

q.append([number[0],0])
q.append([-1*number[0], 0])

while q:
    temp, idx = q.popleft()
    idx += 1
    if idx < n: # 숫자 배열의 크기 만큼만 탐색 idx = 0~4까지 
        q.append([temp+number[idx], idx])
        q.append([temp-number[idx], idx])
    else:
        if temp == target:
            answer += 1
        
print(answer)





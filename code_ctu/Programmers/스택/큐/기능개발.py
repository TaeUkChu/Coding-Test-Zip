# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 1. 걸리는 시간 리스트로 변환
# 2. 걸린 시간 - 다음 인덱스 시간 < 0 이면 cnt +1 , 아니면 cnt = 0 리셋 후 다시 카운트
import math
from collections import deque
def LeftDays(progresses,speeds):
    return deque([math.ceil((100-x)/y) for x,y in zip(progresses,speeds)])

left_day1 = LeftDays([93, 30, 55],[1, 30, 5]) # [7, 3, 9]
left_day2 = LeftDays([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]) # [5, 10,1,1,20,1]
def solution(left_days):
    answer = []
    max_day = left_days.popleft()
    cnt = 1
    while left_days :
        day = left_days.popleft()
        if day > max_day :
            print(cnt)
            answer.append(cnt)
            max_day = day
            cnt=1
        else :
            cnt += 1
    answer.append(cnt)
    return answer

ans = solution(left_day1)
print(ans)

# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
            print(Q)
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

solution([93, 30, 55],[1, 30, 5])
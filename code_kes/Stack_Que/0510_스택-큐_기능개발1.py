from collections import deque

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

day_list = deque(maxlen=len(progresses))
answer = []

for i in range(len(progresses)):
    remaining = 100 - progresses[i]
    if remaining % speeds[i] != 0:
        complete_day = (remaining // speeds[i]) + 1
        day_list.append(complete_day)
    
    elif remaining % speeds[i] == 0:
        complete_day = remaining // speeds[i]
        day_list.append(complete_day)

index = 0        
for i in range(len(day_list)): 
    if day_list[index] < day_list[i]:
        answer.append(i-index) # 각 기능에서 배포의 가능한 기능의 수는 인덱스 차이로 계산 함
        index = i # 현재 배포한 기능 배포일수 보다 더 큰 배포일수로 인덱스를 갱신
        
answer.append(len(day_list) - index) # 갱신된 인덱스부터 마지막 인덱스까지의 개수

print(answer)
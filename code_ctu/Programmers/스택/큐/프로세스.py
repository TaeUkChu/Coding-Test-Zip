# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# 1. deque로 선언
# 2. max_priorities를 찾을 때 까지 돌리기
# 3. 찾으면 popleft 후 다시 돌리기

from collections import deque

priorities = [1, 1, 1, 2]
location = 2
answer=0

priorities = deque([[index,priority] for index, priority in enumerate(priorities)])
max_priority = max(priorities, key=lambda x: x[1])

while priorities :
    if priorities[0][1] != max_priority[1]:
        priorities.rotate(-1)
    else :
        cur_location = priorities.popleft()
        answer+=1
        if priorities :
            max_priority = max(priorities, key=lambda x: x[1])
        if cur_location[0] == location:
            break

print(answer)
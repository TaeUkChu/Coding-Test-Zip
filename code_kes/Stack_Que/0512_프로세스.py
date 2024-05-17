from collections import deque

priorities = [1,9,9]
idx = list(range(len(priorities)))

priorities = deque(priorities)
idx = deque(idx)
location = 0

first = max(priorities)
complete_list = []

while priorities:
    if first > priorities[0]:
        back1 = priorities.popleft()
        back2 = idx.popleft()
        priorities.append(back1)
        idx.append(back2)
    
    elif first == priorities[0]:
        priorities.popleft()
        complete = idx.popleft()
        complete_list.append(complete)
        
        if len(priorities) != 0:
            first = max(priorities)
            
        else:
            break

answer = complete_list.index(location)+1

print(answer)
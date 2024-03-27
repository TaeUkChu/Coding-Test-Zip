from collections import deque
deq = deque(enumerate([-1,1,-1,1,-1],start=1))
deq = deque(enumerate([3,2,1,-3,-1],start=1))

 # 3,2,1,-3,-1
deq.popleft()[0]
deq.rotate(2) #-3 가정
print(deq.popleft()[0], deq) #4
deq.rotate(0)# -1 가정
print(deq.popleft()[0], deq) #5
deq.rotate(0) # 1 가정
print(deq.popleft()[0], deq) #3
deq.rotate(-1)# 2 가정
print(deq.popleft()[0], deq) #2

# rule(deq,3)

# input_list = deque(enumerate(map(int,"-1 1 -1 1 -1".split(" "))))
# print(input_list)
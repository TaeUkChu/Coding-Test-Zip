# 문제 : https://www.acmicpc.net/problem/10845
import sys 
N = int(sys.stdin.readline())

class Queue:
    def __init__(self, capacity) -> None:
        self.front_idx = 0 # 틀림
        self.back_idx = 0 # 틀림
        self.capacity = capacity
        self.array = [None]*capacity
        
    def empty(self):
        if self.front_idx == self.back_idx:
            return 1
        else:
            return 0
        
    def push(self, item):
        # if self.back_idx < self.capacity:
        if self.back_idx == self.capacity-1:
           self.back_idx += 1
           self.array[self.back_idx] = item
        else:
           pass
    
    def pop(self):
        if not self.empty():
            self.front_idx += 1
            item = self.array[self.front_idx]
            self.array[self.front_idx] = None
            return item
        else: return-1
            
        
    def size(self):
        return self.back_idx - self.front_idx
    
    def front(self):
        if self.empty():
            return -1
        return self.array[self.front_idx+1]
    
    def back(self):
        if self.empty():
            return -1
        return self.array[self.back_idx]
    

q = Queue(N)

for i in range(N):
    ord_li = sys.stdin.readline().split()
    
    if len(ord_li) == 2:
        getattr(q,ord_li[0])(int(ord_li[1]))
    else:
        print(getattr(q,ord_li[0])())

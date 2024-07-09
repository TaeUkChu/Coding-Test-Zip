# 문제 : https://www.acmicpc.net/problem/10828
import sys 
N = int(sys.stdin.readline())

class Stack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.array = [None]*capacity
        self.idx = -1
        
    def push(self, item):
        if not self.idx == self.capacity-1:
            self.idx += 1
            self.array[self.idx] = item
        else: pass
    
    def pop(self):
        if not self.empty():
            item = self.array[self.idx]
            self.idx -= 1
            return item
        else: 
            return -1
        
    def size(self): return self.idx+1
    
    def empty(self):
        if self.idx == -1:
            return 1
        else:
            return 0
    
    def top(self):
        if not self.empty():
            return self.array[self.idx]
        else:
            return -1
    

s = Stack(N)
for i in range(N):
    ord_li = sys.stdin.readline().split()
    
    if len(ord_li) == 2:
        getattr(s,ord_li[0])(int(ord_li[1]))
    else:
        print(getattr(s,ord_li[0])())


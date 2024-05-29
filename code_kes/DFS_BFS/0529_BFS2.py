# 문제 : https://www.acmicpc.net/problem/24445
# 정리 : https://velog.io/@uiseoo/백준-알고리즘-수업-너비-우선-탐색-2실버2-24445

import sys
from queue import Queue

input = sys.stdin.readline
n,m,r = map(int, input().split(" "))

visited = [False]*(n+1)
answer = [0]*(n+1)
order = 1 

graph = [[] for i in range(n+1)]

for i in range(m):
    u, v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort(reverse=True)

def BFS2(s):
    global order
    
    q = Queue()
    q.put(s)
    visited[s] = True
    answer[s] = order
    order +=1

    while not q.empty():
        v = q.get()
        for i in graph[v]:    
            if visited[i] == False:
                q.put(i)
                visited[i] = True
                answer[i] = order
                order +=1


BFS2(r)
for i in range(1, n+1):
    print(answer[i])



    
    






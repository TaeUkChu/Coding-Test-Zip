# 문제 : https://www.acmicpc.net/problem/24444
# 정리 : https://velog.io/@uiseoo/백준-알고리즘-수업-너비-우선-탐색-1실버2-24444
from queue import Queue
import sys
input = sys.stdin.readline
n, m, r = map(int, input().split(" "))

visited = [False]*(n+1)
answer = [0]*(n+1)
order = 1

graph = [[] for i in range(n+1)]

# 인접리스트 만들기
for i in range(m):
    u,v = map(int, input().split(" "))
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort()

def BFS(s):
    global order
    q = Queue()
    q.put(s)
    visited[s] = True
    answer[s] = order
    order += 1
    
    while not q.empty():
        v = q.get()         
        for i  in graph[v] :
            if visited[i] == False: 
                q.put(i)
                visited[i] = True
                answer[i] = order
                order += 1
                
BFS(r)

for i in range(1, n+1):
    print(answer[i])

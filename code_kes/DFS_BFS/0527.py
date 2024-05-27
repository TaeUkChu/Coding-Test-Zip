# 문제 : https://www.acmicpc.net/problem/24480
# 정리 : https://velog.io/@uiseoo/백준-알고리즘-수업-깊이-우선-탐색-2실버2-24480

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
n, m, r = map(int, input().split(" ")) 

visited = [False]*(n+1)
answer = [0]*(n+1) 
order = 1

graph = [[] for i in range(n+1)]
for i in range(m):
    u,v = map(int, input().split(" ")) 
    graph[u].append(v)
    graph[v].append(u)
    
for i in graph:
    i.sort(reverse=True)
    

def DFS2(s):
    global order
    
    if not visited[s]:
        visited[s] = True    
        answer[s] = order
        order += 1
        
        for v in graph[s]:
            if not visited[v]:
                DFS2(v)
    else: 
        answer.append(0)

DFS2(r)

for i in range(1, n+1):
    print(answer[i])

        


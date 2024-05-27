# 문제 : https://www.acmicpc.net/problem/24479
# 참고 : https://david-kim2028.tistory.com/entry/%EB%B0%B1%EC%A4%80-24479%EB%B2%88-DFS%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90 
# 정리 : https://velog.io/@uiseoo/백준-알고리즘-수업-깊이-우선-탐색-1실버2-24479

import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m, r = map(int, input().split(" ")) 

# 방문이력을 표현한 배열 생성
visited = [False] * (n+1)
answer = [0] * (n+1)

# 그래프 그리기
graph = [[] for i in range(n+1)] 
for i in range(m):
    u, v = map(int, input().split(" ")) # 정점 u, v 사이의 간선 정보
    graph[u].append(v) # 정점 u와 v는 간선이 있다.
    graph[v].append(u) # 정점 v와 u는 간선이 있다. 

# 인접 정접의 오름차순 방문을 위한 정렬
for i in range(n+1):
    graph[i].sort()


def DFS(x):
    global order
    
    visited[x] = True
    answer[x] = order
    order += 1 
    
    for y in graph[x]:
        if not visited[y]:
            DFS(y)
            
order =1 
DFS(r)

for i in range(1, n+1):
    print(answer[i])
            
        

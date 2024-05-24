
import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n, m, r = map(int, input().split(" ")) 


# range(n+1)은 1부터 n까지 시작하는 그래프의 정점을 표현하기 위해서이다.
graph = [[] for i in range(n+1)] 

visited = [False] * (n+1)
answer = [0] * (n+1)

for i in range(m):
    u, v = map(int, input().split(" ")) # 정점 u, v 사이의 간선 정보
    graph[u].append(v) # 정점 u와 v는 간선이 있다.
    graph[v].append(u) # 정점 v와 u는 간선이 있다. 

# 인접 정접은 오름 차순으로 방문한다.
for i in range(n+1):
    graph[i].sort()


# 각 정점들과 인접한 정접들의 리스트
# [
    # 0   [],
    # 1   [2, 4],
    # 2   [1, 3, 4],
    # 3   [2, 4],
    # 4   [1, 2, 3],
    # 5   []
#    ]

# DFS 함수 작성
# 우선 탐색으로 노드를 방문할 경우
# 노드의 방문 순서를 출력하자.
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
            
        

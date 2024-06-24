# https://school.programmers.co.kr/learn/courses/30/lessons/86971

# tree 구조인 걸 이용 > graph 형태로 변환하기 > DFS 탐색? > 최솟값 차이 찾기

def dfs(graph, cur_v, visited):
    visited[cur_v] = True
    cnt = 1
    for v in graph[cur_v]:
        if not visited[v] :
            cnt += dfs(graph, v, visited)
    return cnt
from collections import deque

def bfs(graph, start,visited):
    deq = deque([start])
    visited[start] = True
    count = 1

    while deq :
        cur_v = deq.popleft()
        for v in graph[cur_v] :
            if not visited[v] :
                deq.append(v)
                visited[v] = True
                count+=1

    return count


def solution(n, wires):
    answer = 1e9

    # 1~n까지 반복해서 간선을 차례로 제거
    for i in range(len(wires)):
        visited = [False]*(n+1)
        # graph 만들기
        graph = {i:[] for i in range(1,n+1)}
        for j in range(len(wires)):
            if i == j : # 제거한 간선이라면 pass
                continue
            v1,v2 = wires[j]
            graph[v1].append(v2)
            graph[v2].append(v1)
        print(graph)

        #dfs 탐색 : 연결 안된 간선까지 탐색
        #first_network = dfs(graph=graph,cur_v=1,visited=visited)
        first_network = bfs(graph=graph,start=1,visited=visited)
        answer = min(answer,abs(n - 2*first_network))

    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))

# BFS
def bfs(graph, start, visited=[]) :
    deq = deque([start])
    while deq :
        cur_v = deq.popleft()
        for v in graph[cur_v]:
            if v not in visited :
                visited.append(v)
                deq.append(v)
    return visited

# DFS
def dfs(graph, cur_v, visited=[]) :
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited :
            visited = dfs(graph, v, visited)
    return visited
# 생능 출판사: 초격차 자료구조와 알고리즘 with 파이썬(2023)
# 8장. 그래프



#=========================================================
# 코드 8.1: 깊이 우선 탐색(인접행렬 방식)

def DFS(vtx, adj, s, visited) :
    
    print("정점 :",vtx,"인접행렬 :",adj,"시작정점 :",s,"방문 여부 :",visited)
    print("현재 정점 :",vtx[s], end=' ') # 현재 정점vtx는 방문 했으므로, 화면에 출력하고        
    visited[s] = True                  # 방문 여부에 시작 시작 정점 s를 True로 갱신 
            
    for v in range(len(vtx)) :         # 정점vtx 개수 만큼 방문
        if adj[s][v] != 0 :            # 간선이 있고
            if visited[v]==False:      # 방문 이력이 없으면
                DFS(vtx, adj, v, visited) # 다시 DFS 호출


#=========================================================
# 코드 8.2: 깊이 우선 탐색 테스트 프로그램

vtx = ['U','V','W','X','Y']     # 그림 8.9의 정점 리스트
edge= [[0,  1,  1,  0,  0],     # 그림 8.9의 인접 행렬
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))
print()


# DFS(인접행렬 방식)

def DFS(vtx, adj, s, visited) :
    
    print("정점 :",vtx,"인접행렬 :",adj,"시작정점 :",s,"방문 여부 :",visited)
    print("현재 정점 :",vtx[s], end=' ') # 현재 정점vtx는 방문 했으므로, 화면에 출력하고        
    visited[s] = True                  # 방문 여부에 시작 시작 정점 s를 True로 갱신 
            
    for v in range(len(vtx)) :         # 시작정점 부터 시작해서 정점 개수 v만큼 방문
        if adj[s][v] != 0 :            # 간선이 있고
            if visited[v]==False:      # 방문 이력이 없으면
                DFS(vtx, adj, v, visited) # 다시 DFS 호출


vtx = ['U','V','W','X','Y']     
edge= [[0,  1,  1,  0,  0],   
       [1,  0,  1,  1,  0],
       [1,  1,  0,  0,  1],
       [0,  1,  0,  0,  0],
       [0,  0,  1,  0,  0]]

print('DFS(출발:U) : ', end="")
DFS(vtx, edge, 0, [False]*len(vtx))


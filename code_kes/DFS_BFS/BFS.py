# BFS 너비 우선 탐색(인접 리스트 방식)

from queue import Queue                 
def BFS_AL(vtx, aList, s):
    n = len(vtx)                        
    visited = [False]*n                 
    Q = Queue()                         
    Q.put(s)                            
    visited[s] = True                   
    while not Q.empty() :
        s = Q.get()                     
        for v in aList[s] :             
            if visited[v]==False :      
                Q.put(v)                
                visited[v] = True       


vtx = ['U','V','W','X','Y']     # 정점 리스트
aList=[[1, 2],                  # 인접 리스트
       [0, 2, 3],   
       [0, 1, 4],
       [1],
       [2]]

print('BFS_AL(출발:U): ', end="")
BFS_AL(vtx, aList, 0)
print()

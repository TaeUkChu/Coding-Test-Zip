N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0 # k와 비교할 교환횟수
result = ''
    
for i in range(1,N):
    key=A[i]
    j = i-1
    while j>=0 and A[j]>key:
        A[j+1] = A[j]
        cnt += 1
        j -= 1
    A[j+1] = key        
    if cnt == K:
        result = A.copy()
    
    
if cnt < K:
    print(-1)
else :   
    for j in result:
                print(j, end=' ')
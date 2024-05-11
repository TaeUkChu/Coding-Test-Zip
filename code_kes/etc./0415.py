N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0 
result = ''
    
for i in range(2,N):
    key=A[i]                     # 삽입할 요소
    j = i-1                      # 삽입할 요소의 앞 요소의 인덱스
    while 0 <= j and A[j] > key: # 앞요소가 삽입요소보다 크고 앞요소 인덱스가 0이 될때 까지
        A[j+1] = A[j]            # 조건에 충족 되면 앞요소 +1 인덱스에 요소를 복사(뒤로 밀기)
        j -= 1                   # 앞요소 인덱스를 -1(=앞앞요소)하여 재갱신
        cnt += 1
        if cnt == K:
            result = A.copy()    
    A[j+1] = key                 # 삽입요소가 앞요소보다 크거나(or) 앞요소 인덱스가 -1 이면          
    cnt += 1                     # 앞요소 다음 위치에 삽입요소 선택삽입!
    
if cnt < K:
    print(-1)
else :   
    for j in result:
                print(j, end=' ')
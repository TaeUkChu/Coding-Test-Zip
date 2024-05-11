N, K = map(int, input().split())
A = list(map(int, input().split()))
# A = input().split()
# A = [int(x) for x in A]

cnt = 0 # k와 비교할 교환횟수
result = ''

for i in range(N-1):
    # 가장 큰 수 i를 찾는다. => 큰수의 인덱스 찾기
    # range_check = A[:N-i]
    # max_num = max(A[:N-i])
    max_index= A.index(max(A[:N-i]))
    if  A[max_index] != A[-1-i]:
        A[max_index], A[-1-i] = A[-1-i], A[max_index] # 범위 갱신
        cnt += 1 
        if cnt == K:
            result = A.copy()
    else: 
        pass
if cnt < K:
    print(-1)
else :   
    for j in result:
                print(j, end=' ')
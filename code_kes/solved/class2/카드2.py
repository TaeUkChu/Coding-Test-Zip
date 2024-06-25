# 문제 : https://www.acmicpc.net/problem/2164

from collections import deque
n=int(input())
q=deque(range(1, n+1))

ans=[]

while q:
    ans.append(q.popleft())
    if q:
        q.append(q.popleft())

print(ans[-1])


# while q:
#     ans.append(q.popleft())
#     q.append(q.popleft()) 
# problem
# 마지막 첫요소가 q에 있기에 whil문은 진행
# ans.append(q.popleft())까지는 코드가 진행되지만
# 비로소 빈 q가 되었기 때문에  q.append(q.popleft())을 수행하지 못하고 인덱스 에러가 발생

# solution
# 마지막 첫요소의 경우를 위해 
# 실행 전 q가 빈큐인지 한번더 확인하는 코드 추가
# q.append(q.popleft())

# print(ans[-1])
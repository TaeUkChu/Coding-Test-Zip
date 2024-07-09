# 문제 : https://www.acmicpc.net/problem/11866

n, k = map(int, input().split(" "))
from collections import deque
         
q = deque(range(1, n+1))

ans = []
while q:
    for i in range(k-1):
        q.append(q.popleft())        
    ans.append(q.popleft())
        
ans = "<" + ", ".join(map(str, ans)) + ">"
print(ans)


# ans = []
# while q:
#     for i in range(k):
#         if i == 2: 
#             temp = q.popleft()
#             ans.append(temp)
#         else:
#             temp = q.popleft()
#             q.append(temp)
# ans = "<" + ", ".join(map(str, ans)) + ">"
# print(ans)
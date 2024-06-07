# 문제 : https://www.acmicpc.net/problem/1978
# 정리 : 

import math
n = int(input())
arr = list(map(int, input().split()))
cnt = 0


# 참고 코드 
for i in arr:
    for j in range(2, i+1):
        if i%j == 0: 
            if i == j: 
                cnt += 1
            
            break
print(cnt)
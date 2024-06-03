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

# 정답 코드
def isPrime(a):
    if (a<2):
        return False
    for i in range(2, a):
        if a%i == 0:
            return False
    return True

for i in range(n):
    if isPrime(arr[i]):
        cnt += 1
    else:
        pass

print(cnt)

# 제곱근을 이용한 코드 
def isPrime2(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

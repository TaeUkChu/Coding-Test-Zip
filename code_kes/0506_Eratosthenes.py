# 소수 : 1과 그 자신 이외의 자연수로는 나눌 수 없는 자연수
# 약수 : 나누어 떨어지게 하는 수
# - 약수는 무조건 1~n^의 범위에 존재한다.

n = 10
a = [False, False] + [True]*(n-1)
primes=[]

for i in range(2, n+1):
    if a[i]: # 2번 a[i] True이면
        primes.append(i)
        for j in range(2*i, n+1, i): # 1번 i의 간격으로, 2인 경우 2의 간격(2의 배수) 소수가 아닌 것을 False n=10의 범위에서 소수가 아닌것을 가려냄
            a[j] = False

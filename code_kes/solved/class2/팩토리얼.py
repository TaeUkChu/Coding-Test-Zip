# 문제 : https://www.acmicpc.net/problem/1676

def fac(n):
    if n == 0:   
        return 1 
    
    else:
        result = n
        for i in range(1,n):
            result = result * (n-i)
        return result

n = int(input())

factorial = str(fac(n))
li =list(factorial)[::-1]

idx = 0
while li[idx]== "0":
        idx += 1

print(idx)
    
    
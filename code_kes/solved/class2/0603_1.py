# 문제 : https://www.acmicpc.net/problem/1546
# 정리 : https://velog.io/@uiseoo/백준-평균브론즈1-1546

n = int(input())
arr = list(map(int, input().split(" ")))
high = max(arr)

for i in range(n):
    arr[i] = (arr[i]/high)*100
    
aver = sum(arr)/len(arr)

print(aver)
# print(60/80 * 100)


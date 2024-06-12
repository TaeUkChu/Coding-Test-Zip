# 문제 : https://www.acmicpc.net/problem/1436

n = int(input())
cnt = 0
series = 666

while True:
    if "666" in str(series):
        cnt += 1
        
    if cnt == n:
        break
    
    series += 1

print(series)
        

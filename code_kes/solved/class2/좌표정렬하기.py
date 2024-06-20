# 문제 : https://www.acmicpc.net/problem/11650


# 선택정렬

N = int(input())

li = []

for i in range(N):
    x, y = map(int, input().split(" "))
    li.append([x,y])

leng = len(li)

for i in range(leng-1):
    least = i
    
    for j in range(i+1, leng):
        if li[least][0] > li[j][0]:
            least = j
        
        elif li[least][0] == li[j][0]:
            if li[least][1] > li[j][1]:
                least = j
                
    li[i], li[least] = li[least], li[i]      
    
for answer in li:
    print(answer)  
    
# 퀵정렬

N = int(input())

li = []

for i in range(N):
    x, y = map(int, input().split(" "))
    li.append([x,y])
    
    
def quick(arr):
    
    if len(arr) <= 1:
        return arr
    
    pivot =arr[len(arr)//2]
    
    left = [x for x in arr if x[0] < pivot[0]]
    middle = [x for x in arr if x[0] == pivot[0]]
    middle.sort(key=lambda x : x[1])
    right = [x for x in arr if x[0] > pivot[0]]
    
    return quick(left) + middle + quick(right)

for answer in quick(li):
    print(answer[0], answer[1])


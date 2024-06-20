# 퀵정렬

def quick(arr):
    
    if len(arr) <= 1: # 종료 조건
        return arr
    
    pivot =arr[len(arr)//2]
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    # middle.sorit(key=x[1])
    right = [x for x in arr if x > pivot]
    
    return quick(left) + middle + quick(right)

arr =  [3, 6, 8, 10, 1, 2, 1]

print(quick(arr))


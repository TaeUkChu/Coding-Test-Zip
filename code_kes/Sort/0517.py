def selection_sort(arr):    
    n = len(arr)    
    
    for idx in range(n-1): 
        least = idx        
        
        for next_idx in range(idx+1, n): 
            if arr[next_idx] < arr[least]:
                least = next_idx    
                        
        arr[idx], arr[least] = arr[least], arr[idx]
    
    return arr

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for command in commands:
    i, j, k = command
    
    arr = array[i-1:j]
    sorted_arr = selection_sort(arr)
    
    order = sorted_arr[k-1]
    answer.append(order)

# import sys
# input = sys.stdin.readline

def five(N):
    
    count = 0
    while N >= 5:
        count += N//5
        N //= 5
        
    return count
   

print(five(250)) 
            
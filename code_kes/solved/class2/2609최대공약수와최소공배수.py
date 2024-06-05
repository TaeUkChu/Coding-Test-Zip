a, b = map(int, input().split(" "))

def divisor(n):
    divisor_li = []
    
    for i in range(1, n+1):
        if n%i == 0 :
            divisor_li.append(i)
            
    return divisor_li

def FindGCD(arr1, arr2):
    GCD = []
    
    if arr1 > arr2:
        for i in arr2:
            for j in range(len(arr1)):
                if i == arr1[j]:
                    GCD.append(i)
            
    elif arr1 < arr2:
        for i in arr1:
            for j in range(len(arr2)):
                if i == arr2[j]:
                    GCD.append(i)
    
    return max(GCD)

def FindLCM(a, b):
    return abs(a*b) // gcd
        
a_li = divisor(a)
b_li = divisor(b)
gcd = FindGCD(arr1=a_li, arr2=b_li)
lcm = FindLCM(a,b)

print(gcd, lcm)
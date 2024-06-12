# 문제 : https://www.acmicpc.net/problem/28702

# 입력
a, b, c = input(), input(), input()
x = 0

# 1. 앞 항에 대한 숫자열 문자열 구분 함수 작성(str, int 변환 가능 여부)

def int_str(n):
    try:
        n = int(n)
        return n
    except:
        return n
    
# 앞항이 숫자열, 혹은 문자열이라면
def fb_int(n, idx):
    global x

    try:
        x = n+1
        
        if x % 3 == 0 and x % 5 == 0:
            return "FizzBuzz"
        
        elif x % 3 == 0:
            x = "Fizz"
            return x
        
        elif x % 5 == 0:
            x = "Buzz"
            return x
        
        elif not x % 5 == 0 or x % 5 == 0:
            return x
        
    except:
        idx -= 1    
        n = fb_int(li[idx], idx)
    
        return 
        

a, b, c = int_str(a), int_str(b), int_str(c)
idx = -1
li = [a,b,c]

x = fb_int(li[idx], idx)

print(x)
 
 # print(type(a), type(b), type(c))
        
# a = "19823"
# a = int_str(a)
# print(a, type(a))

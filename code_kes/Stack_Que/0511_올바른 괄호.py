def solution(s):
    
    s = list(s)
    answer = True
    stack = []
    for i in s:
        if i == "(" :
            stack.append(i)
        elif i == ")":
            if len(stack) == 0: # 조건1
                answer = False
            else : 
                left = stack.pop() # 조건2
                if i == ")" and left != "(":
                    answer = False 
                
    if len(stack) != 0: # 조건 3 
        answer = False

    return answer
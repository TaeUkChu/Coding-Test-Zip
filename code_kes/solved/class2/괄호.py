# 문제 : https://www.acmicpc.net/problem/9012
# 스택 : 후입선출, 늦게들어온 것이 먼저 나간다.

n = int(input())


for i in range(n):
    ps = input()
    stack = []

    for j in ps:
        if j == ')':
            if not stack:
                print('NO')
                break
            elif stack.pop() == ')': 
                print('No')
                break        
        else:
            stack.append(j)
    else:
        if not stack:
                    print("YES")
        else :
            print("NO")
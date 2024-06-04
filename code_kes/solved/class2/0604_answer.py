# 슬라이싱을 이용해 풀기

while True:
    n = input()
    
    if n == "0":
        break
    
    if n == n[::-1]:
        print("yes")
    else:
        print("no")

# stack을 활용해서 풀기
while True:
    num = input()
    stack = []
    reverse_num = ''

    if num == '0':
        break

    for i in num :
        stack.append(i)

    for j in range(len(num)):
        reverse_num += stack.pop()

    if reverse_num == num :
        print("yes")
    else: 
        print("no")
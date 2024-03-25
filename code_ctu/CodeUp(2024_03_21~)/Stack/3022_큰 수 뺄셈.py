'''
입력
큰 수 a, b가 두 줄에 걸쳐 입력된다. (a, b는 100자리 이하)

출력
a-b의 결과를 출력한다.

입력 예시
11232412
3

출력 예시
11232409
'''

a = list(map(int,input()))
b = list(map(int,input()))
bo = False

if len(a)>len(b):
    b = [0]*(len(a)-len(b)) + b
elif len(a)<len(b):
    a = [0]*(len(b)-len(a)) + a

stack = []
ten = 0

for i in range(len(a)):
    if a[i] > b[i] :
        bo = False
        break
    elif a[i] == b[i]:
        continue
    else :
        bo = True


while a and b :
    if bo == False:
        one_number_result = a.pop() - b.pop() + ten
    else :
        one_number_result = b.pop() - a.pop() + ten

    ten = one_number_result//10
    one_number_result -= 10
    stack.append(one_number_result)

temp = stack.pop()
try :
    while temp == 0:
        temp = stack.pop()
except :
    temp = 0

if bo :
    print("-",end="")
print(temp,end="")
while stack :
    print(stack.pop(),end="")
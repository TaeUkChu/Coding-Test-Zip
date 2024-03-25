'''
큰 수를 표현할 때 자릿수를 쉽게 구분하기 위해 천단위 구분 기호인 콤마(,)를 사용한다.

어떤 수가 입력되면 천단위 구분 기호를 넣어 그 수를 다시 출력하는 프로그램을 작성하시오.

입력 예시
8
12421421

출력 예시
12,421,421
'''

n = int(input())
number = list(input())
stack = []
for i in range(1,n+1):
    stack.append(number.pop())
    if i%3 == 0:
        stack.append(',')

if stack[-1] == ',' :
    stack.pop()

while(stack):
    print(stack.pop(),end="")

'''
int는 32비트, long long 은 64비트라서 이 보다 더 큰 숫자는 저장할 수 없다.

아주 큰 숫자의 덧셈을 하려고 한다.

계산 결과를 출력하시오.

입력
첫째줄과 둘째줄에 큰 수 a, b가 입력된다. (a, b는 100자리 이하의 정수)
출력
큰 수 덧셈의 결과를 출력한다.

입력 예시
12345678910111213
2839287

출력 예시
12345678912950500
'''

a = list(map(int,input()))
b = list(map(int,input()))
if len(a)>len(b):
    b = [0]*(len(a)-len(b)) + b
else :
    a = [0]*(len(b)-len(a)) + a

stack = []
ten = 0
while a and b : # 1 / 0 / 2
    one_number_result = a.pop() + b.pop() + ten
    ten = one_number_result//10
    one_number_result %= 10
    stack.append(one_number_result)

if ten == 1:
    stack.append(1)
while stack:
    print(stack.pop(),end="")


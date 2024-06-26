'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.

입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

입력
입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다.
입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

출력
출력은 표준 출력을 사용한다.
만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

예제 입력 2
3
((
))
())(()

예제 출력 2
NO
NO
NO
'''

# ( 이 나오면 스택에 넣고 )가 나오면 (를 pop으로 빼내기
t = int(input())

answer = ""
answer_stack=[]
for _ in range(t):
    stack = []
    vps = input()
    for ch in vps :
        try :
            if ch == "(" :
                stack.append(ch)
            elif ch == ")" :
                stack.pop()
        except : # 빈 스택에 pop 하는 것에 대한 예외처리
            stack = [0]
            break
    if not stack :
        answer = "YES"
    else :
        answer = "NO"
    answer_stack.append(answer)

for i in range(t):
    print(answer_stack[i])

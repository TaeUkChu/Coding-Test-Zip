# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque

arr = [1,1,3,3,0,1,1] #ans = 1,3,0,1
answer = []
deq = deque(arr)
while deq :
    num = deq.popleft()
    if not answer or num != answer[-1]:
        answer.append(num)
print(answer)


# 다른 사람 풀이
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] != [i]: a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
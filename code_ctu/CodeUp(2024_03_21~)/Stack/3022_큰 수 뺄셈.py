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
bo = False #b가 더 클 경우 true

# 자릿수 맞춰주기
if len(a)>len(b):
    b = [0]*(len(a)-len(b)) + b
elif len(a)<len(b):
    a = [0]*(len(b)-len(a)) + a

#어떤 수가 더 큰지 or 작은지 확인
for i in range(len(a)):
    if a[i] > b[i] :
        bo = False
        break
    elif a[i] == b[i]:
        continue
    else :
        bo = True
        break

#한 자리마다 계산
for i in range()
# https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 접근 방식 : 가장 앞 부터 큰 수 뽑기 (성공)
# 큰 수가 있다면 앞 숫자들 작은 거 지우기
# 새로운 수가 등장할 때 마다 이전 수의 뒤부터 더 큰 수가 나올 때 까지 삭제

# 접근 방식 2 : 가장 작은 값 없애기. (실패)
# 작은 값들만 제거한다고 가장 큰 수가 되는게 아님.
# ex. 반례 4177252841, 4 :
#   결괏값 "477584"
#   기댓값 "775841"
def solution(number, k):
    answer = []
    for num in number:
        while k > 0 and answer and num > answer[-1]:
            answer.pop()
            k-=1
        answer.append(num)

    if k > 0:
        answer = number[:-k]

    return ''.join(answer)

number = "41772528841"
k = 7

print(solution(number,k))
# answer = 3234
# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3

# 제일 큰 숫자를 fix, 전 범위 순회하면서 두번 째 숫자 중 가장 큰 값 선택
def solution(sizes):
    answer, max_size, second_size = 0,0,0
    for wallet in sizes :
        if wallet[0] < wallet[1]:
            temp = wallet[0]
        else :
            temp = wallet[1]
        max_size = max(max_size, max(wallet))
        second_size = max(second_size, temp)
    answer = max_size * second_size
    return answer
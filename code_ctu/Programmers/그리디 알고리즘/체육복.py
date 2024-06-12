# https://school.programmers.co.kr/learn/courses/30/lessons/42862

# lost를 pop 하는 구조로 알고리즘 짜기. << 비효율적 by GodGPT

def solution(n, lost, reserve):
    answer = 0

    # 여벌이 있는 사람이 잃어버린 경우 선 제거
    reserve = set(reserve) - set(lost)
    lost = set(lost) - set(reserve)
    reserve = sorted(reserve)

    for r in reserve :
        if r-1 in lost :
            lost.remove(r-1)
        elif r+1 in lost :
            lost.remove(r+1)
    answer = n - len(lost)
    return answer


n = 5
lost = [2,4]
reserve = [1,3,5]

print(solution( 5, [4, 2], [3, 5]))
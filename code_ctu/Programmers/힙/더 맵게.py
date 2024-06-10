# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 정렬 후 0,1번 인덱스 계산 -> 스코빌 지수 구하기
# 스코빌 지수 > K 일 때 까지 반복

"""  Python의 heapq 모듈은 최소 힙(min-heap)으로 구현되어 있으며,
 이는 부모 노드가 항상 자식 노드보다 작거나 같은 값을 갖는 특성을 가집니다. """
import heapq

scoville = [1,2,3,9,10,12]
K = 7

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) > 1:  # 최소 두 개 이상의 요소가 있을 때까지 반복
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        second = heapq.heappop(scoville)
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1

    # 마지막으로 남은 하나의 요소가 조건을 충족하는지 확인
    if len(scoville) == 1 and scoville[0] >= K:
        return answer
    else:
        return -1

print(solution(scoville,K))
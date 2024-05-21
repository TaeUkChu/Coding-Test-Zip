# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 정렬 후 0,1번 인덱스 계산 -> 스코빌 지수 구하기
# 스코빌 지수 > K 일 때 까지 반복

"""  Python의 heapq 모듈은 최소 힙(min-heap)으로 구현되어 있으며,
 이는 부모 노드가 항상 자식 노드보다 작거나 같은 값을 갖는 특성을 가집니다. """
import heapq

scoville = [1,2,3,9,10,12]
K = 7


def solution(scoville, K):
    answer = 0
    s_point = 0
    heapq.heapify(scoville)

    while len(scoville) > 1 :
        s_point = heapq.heappop(scoville) + heapq.heappop(scoville)*2
        smallest = heapq.heappushpop(scoville,s_point)
        answer+=1
        if smallest >= K :
            return answer
    return -1

print(solution(scoville,K))